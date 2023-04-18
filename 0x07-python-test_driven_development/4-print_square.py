#!/usr/bin/python3
""" module for print_square method """
def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an interger")
    if size < 0:
        raise ValueError("size  must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an  interger")
""" looping the sixe """
    for i range(size):
        print ("#" * size)
