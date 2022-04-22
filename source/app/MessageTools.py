import json
import time
import datetime
import uuid
import hmac
import hashlib
import requests
import platform

protocol = 'https'
domain = 'api.coolsms.co.kr'
prefix = ''

key_path = '../data/apikey.json'
with open(key_path) as f:
    key_json = json.load(f)

api_key = key_json['API-KEY']
api_secret = key_json['API-SECRET']

preview_path = '../data/Message.json'
with open(preview_path, encoding='utf-8') as f:
    preview_json = json.load(f)

deliveryNotice = 0

message_type = {
    0: "delivery notice"
}


def unique_id():
    return str(uuid.uuid1().hex)


def get_iso_datetime():
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
    return datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()


def get_signature(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()


def get_headers():
    date = get_iso_datetime()
    salt = unique_id()
    combined_string = date + salt

    return {
        'Authorization': 'HMAC-SHA256 ApiKey=' + api_key + ', Date=' + date + ', salt=' + salt + ', signature=' +
                         get_signature(api_secret, combined_string),
        'Content-Type': 'application/json; charset=utf-8'
    }


def get_url(path):
    url = '%s://%s' % (protocol, domain)
    if prefix != '':
        url = url + prefix
    url = url + path
    return url


def send_message(parameter):
    parameter['agent'] = {
        'sdkVersion': 'python/4.2.0',
        'osPlatform': platform.platform() + " | " + platform.python_version()
    }

    return requests.post(get_url('/messages/v4/send-many'), headers=get_headers(), json=parameter)


def write_message_data(var: dict, msg_type: int):
    to = var['to']
    from_ = var['from']
    variables = var['msg_var']

    pfId = 'KA01PF210702083619302MtFIFzfLBAB'
    templateId = None

    if msg_type == deliveryNotice:
        templateId = 'KA01TP220420081458677c6jbPtoWyWz'

    data = {
        'to': to,
        'from': from_,
        'kakaoOptions': {
            'pfId': pfId,
            'templateId': templateId,
            'variables': variables
        }
    }

    return data


def show_preview(var: dict, msg_type: int):     # make preview message with message json
    preview_msg = preview_json[message_type[msg_type]]

    return preview_msg.format(list(var['msg_var'].values()))
