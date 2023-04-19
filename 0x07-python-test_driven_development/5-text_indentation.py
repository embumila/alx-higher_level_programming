#!/usr/bin/python3

def text_identation(txt):
    my_string = str(txt)
    start_index = 0
    if type(my_string) != str:
        raise TypeError("text must be string")
    for i,element in enumerate(my_string):
        if not str(element).isalnum() and element in ['?','.',':']:
            print(my_string[start_index:i+1],end='\n\n')
            start_index = i + 1
