import re


def clean_string(string: str) -> str:
    """
    Function that removed leading and trailing whitespace and lower cases all strings.

    :param s: String to be cleaned
    :return: Cleaned string
    """
    string = string.lower()
    string = string.strip(" ")
    string = re.sub(' {2,}', ' ', string)
    return string


def remove_nan_from_list(lst: list) -> list:
    new_list = [string for string in lst if isinstance(string, str)]
    return new_list
