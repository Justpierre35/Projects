#! /usr/bin/env python3

import os
import requests

directory_file = "/data/feedback/"
dict_files = {}
url_post = "http://104.154.185.173/feedback/"


def list_files():
    for name_file in os.listdir(directory_file):
        if name_file.endswith(".txt"):
            with open(directory_file+name_file, "r") as file:
                file_reading = file.read().split("\n")
                dict_file = {}

                dict_file["title"] = file_reading[0]
                dict_file["name"] = file_reading[1]
                dict_file["date"] = file_reading[2]
                dict_file["feedback"] = file_reading[3]
                dict_files[name_file] = dict_file
    return dict_files


def post_request(dict_files):
    for dict_values in dict_files.values():
        print(dict_values)
        response = requests.post(url_post, data=dict_values)
        print(response.status_code)


def main():
    list_files()
    post_request(dict_files)


if __name__ == "__main__":
    main()
