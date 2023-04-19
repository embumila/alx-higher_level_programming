#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    start_index = 0
    if type(text) != str:
        raise TypeError('text must be string')
    for i, element in enumerate(text):
        if element in ["?", ".", ":", "\n\n"]:
            print(text[start_index : i + 1], end="\n\n")
            start_index = i + 1

    # Print the remaining text after the last special character or newline
    if start_index < len(text):
        print(text[start_index:])
