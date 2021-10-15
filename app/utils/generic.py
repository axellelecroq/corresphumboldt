import json

from ..app import *


def get_json(path):
    """
    Get data from a JSON file.
    :param path: str
    :return: data
    :rtype: dict
    """
    with open(path, encoding="iso-8859-15") as data_file:
        data = json.load(data_file)
    return data


def write_json(file, data):
    """
    Store JSON data in a JSON file.
    :param file: str
    :param data: dict
    """
    with open(file, mode="w"):
        json.dump(data, file)
