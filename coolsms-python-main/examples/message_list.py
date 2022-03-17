import requests
import json
import sys
import os.path

sys.path.append('../lib')

import auth
import config

if __name__ == '__main__':
    res = requests.get(config.getUrl('/messages/v4/list'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # limit
    res = requests.get(config.getUrl('/messages/v4/list?limit=10'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # messageId
    res = requests.get(config.getUrl('/messages/v4/list?messageId=XXXXXXX'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # groupId
    res = requests.get(config.getUrl('/messages/v4/list?groupId=XXXXXXX'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 수신번호로 조회
    res = requests.get(config.getUrl('/messages/v4/list?to=01000000001'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 발신번호로 조회
    res = requests.get(config.getUrl('/messages/v4/list?from=029302266'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 메시지타입으로 조회
    res = requests.get(config.getUrl('/messages/v4/list?type=SMS'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 메시지 상태 코드로 조회
    res = requests.get(config.getUrl('/messages/v4/list?statusCode=4000'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 페이지 처리
    page1 = requests.get(config.getUrl('/messages/v4/list?limit=5'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret)).json()
    print(json.dumps(page1, indent=2, ensure_ascii=False))
    if 'nextKey' in res:
      # 읽어올 데이터가 더 있음
      startKey = res['nextKey']
      page2 = requests.get(config.getUrl('/messages/v4/list?limit=5&startKey=%s' % startKey),
                       headers=auth.get_headers(config.apiKey, config.apiSecret)).json()
      print(json.dumps(page2, indent=2, ensure_ascii=False))
    # 페이지 처리
    page1 = requests.get(config.getUrl('/messages/v4/list?limit=5'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret)).json()
