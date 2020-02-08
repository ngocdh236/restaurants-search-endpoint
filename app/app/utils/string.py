import re


def remove_special_characters(string):
    return re.sub("[^\w\s]", "", string)


def is_string_included(string, compare_string):
    return string.lower() in compare_string.lower()
