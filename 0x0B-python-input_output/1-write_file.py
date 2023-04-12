#!/usr/bin/python3


def write_file(filename="", text=""):
    """writing  a string to a file"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
