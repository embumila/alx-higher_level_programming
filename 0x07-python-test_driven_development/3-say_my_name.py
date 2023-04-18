#!/usr/bin/python3

"""Module for say_my_name method"""

def say_my_name(first_name, last_name=""):
    if type(first_name) != string:
        raise TypeErro("first_name must be a string")
    else if type(last_name) != string:
        raise TypeError ("last_name must be  a string")
    print ("My name is{:s}  {:s}".format(first_name + last_name))
