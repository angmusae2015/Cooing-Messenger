from pandas.core.frame import DataFrame


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
