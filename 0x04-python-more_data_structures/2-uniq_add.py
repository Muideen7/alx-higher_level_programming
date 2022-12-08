#!/usr/bin/python3
def uniq_add(my_list=[]):
    r_list = []
    res = 0
    for i in my_list:
        if i not in r_list:
            r_list.append(i)
    for uniqs in r_list:
        res += uniqs
    return res
