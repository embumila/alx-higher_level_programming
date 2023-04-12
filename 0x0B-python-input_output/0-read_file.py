
#!/usr/bin/python3


def read_file(filename=""):
    """ reading the text file (UTF8) and print the stadout """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
