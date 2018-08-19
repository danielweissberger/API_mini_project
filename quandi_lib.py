import math

# This function will retrieve a list of daily stock data from quandi
# (json_dict is a dictionary created from a quandi API response)
def get_daily_data_item(item_num, json_dict):
    return [daily_data[item_num] for daily_data in json_dict['dataset_data']['data']]

# fill_nones will take a zipped list of opn/close data from quandi and fill in None values (using previous)
def fill_nones(zipped_list):
    for index, lst in enumerate(zipped_list):
        if lst[0] == None:
            zipped_list[index][0] = zipped_list[index - 1][1]
        if lst[1] == None:
            zipped_list[index][1] = zipped_list[index][0]

    return zipped_list

# Calculates difference of 2 lists of equal length (elements must be integer/float)
def list_diff(zipped_list):
    return [l1-l2 for l1, l2 in zipped_list]

# Calculates the median of a list
def median(lst):
    lst.sort()
    list_length = len(lst)
    half_length = list_length/2
    if list_length % 2 == 0:
        return (lst[math.floor(half_length)-1] + lst[math.ceil(half_length)]) / 2
    else:
        return lst[math.floor(half_length)]
