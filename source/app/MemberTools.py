import json


path = "../data/Member.json"
with open(path) as f:
    member_list = json.load(f)


class MemberNotFoundError(Exception):
    def __str__(self):
        return "일치하는 회원을 찾을 수 없습니다."


def get_child_name(num: str):
    family_id = num[:2]
    child_id = num[2:]

    try:
        family_info = [family for family in member_list if family['family id'] == family_id][0]
    except IndexError:
        raise MemberNotFoundError()
    else:
        name = [child for child in family_info['children'] if child['num'] == child_id][0]['name']

    return name


"""
def get_child_info(func):
    def wrapper(table: DataFrame, num: str):
        family_ID = num[:2]
        child_ID = num[2:]

        children = table[table['Family ID'] == family_ID]['Child'].values[0]

        for child in children.split('/'):
            if child.split(',')[0] == child_ID:
                return func(child)

    return wrapper


@get_child_info
def get_child_name(child_info: str):
    return child_info.split(',')[1]


@get_child_info
def get_child_level(child_info: str):
    return child_info.split(',')[2]
"""
