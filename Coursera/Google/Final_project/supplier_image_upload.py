#! /usr/bin/env python3

import os
import requests

directory_file = "supplier-data/images/"
url_post = "http://localhost/upload/"


def list_files():
    for name_file in os.listdir(directory_file):
        if name_file.endswith(".jpeg"):
            post_request(name_file)


def post_request(name_file):
    with open(directory_file+name_file, 'rb') as opened:
        r = requests.post(url_post, files={'file': opened})
    print(r.status_code)


def main():
    list_files()


if __name__ == "__main__":
    main()
