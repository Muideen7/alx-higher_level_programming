#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    t = dict(a_dictionary)
    for key, value in t.items():
        t[key] = value * 2
    return t
