import re


def is_string_included(string, compare_string):
    return string.lower() in compare_string.lower()


def remove_special_characters(string):
    return re.sub(r"[^\w\s]", "", string)
