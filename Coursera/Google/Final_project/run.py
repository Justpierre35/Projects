#! /usr/bin/env python3

import os
import requests

directory_file = "supplier-data/descriptions/"
dict_files = {}
url_post = "http://34.69.133.43/fruits/"
summary = []


def list_files():
    for name_file in os.listdir(directory_file):
        if name_file.endswith(".txt"):
            with open(directory_file+name_file, "r") as file:
                file_reading = file.read().split("\n")
                dict_file = {}

                dict_file["name"] = file_reading[0]
                dict_file["weight"] = int(file_reading[1].strip("lbs"))
                dict_file["description"] = file_reading[2]
                dict_file["image_name"] = name_file.replace(".txt", ".jpeg")
                dict_files[name_file] = dict_file
                summary.append("name: {}".format(file_reading[0]))
                summary.append("weight: {}".format(file_reading[1]))
                summary.append(" ")
    return summary


def post_request(dict_files):
    for dict_values in dict_files.values():
        response = requests.post(url_post, data=dict_values)
        print(response.status_code)


def main():
    list_files()
    post_request(dict_files)


if __name__ == "__main__":
    main()
