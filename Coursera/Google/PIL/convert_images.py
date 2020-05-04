#!/usr/bin/env python3
import os
from PIL import Image


def convert_images():

    for name_file in os.listdir("images"):
        if name_file.endswith("48dp"):
            image_file = Image.open("images/"+name_file, mode='r')
            image_file.rotate(90).resize((128, 128)).convert(
                "RGB").save("opt/icons/"+name_file, "JPEG")


def main():
    convert_images()


if __name__ == "__main__":
    main()
