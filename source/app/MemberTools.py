import json


path = "../data/Member.json"
with open(path, encoding='utf-8') as f:
    member_dic = json.load(f)


class MemberNotFoundError(Exception):
    def __str__(self):
        return "일치하는 회원을 찾을 수 없습니다."


def get_child_name(family_id: str, child_id: str):
    try:
        family_info = member_dic[family_id]
    except:
        raise MemberNotFoundError()
    else:
        name = [child for child in family_info['children'] if child['num'] == child_id][0]['name']

    return name


def get_contact(family_id: str):
    contact = member_dic[family_id]['contact']

    return contact
