import math
def get_daily_data_item(item_num, json_dict):
    return [daily_data[item_num] for daily_data in json_dict['dataset_data']['data']]


def fill_nones(zipped_list):
    for index, lst in enumerate(zipped_list):
        if lst[0] == None:
            zipped_list[index][0] = zipped_list[index - 1][1]
        if lst[1] == None:
            zipped_list[index][1] = zipped_list[index][0]

    return zipped_list


def list_diff(zipped_list):
    return [l1-l2 for l1, l2 in zipped_list]


def median(lst):
    lst.sort()
    list_length = len(lst)
    half_length = list_length/2
    if list_length % 2 == 0:
        return (lst[math.floor(half_length)-1] + lst[math.ceil(half_length)]) / 2
    else:
        return lst[math.floor(half_length)]
