#!/usr/bin/env python3

import os
from PIL import Image


def convert_images():

    for name_file in os.listdir("supplier-data/images"):
        if name_file.endswith(".tiff"):
            image_file = Image.open("supplier-data/images/"+name_file,
                                    mode='r')
            name_file = name_file.replace(".tiff", ".jpeg")
            image_file.resize((600, 400)).convert(
                "RGB").save("supplier-data/images/"+name_file, "JPEG")


def main():
    convert_images()


if __name__ == "__main__":
    main()
