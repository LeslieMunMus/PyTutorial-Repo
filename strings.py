def main():
    message = "Hello World"
    print(message)
    print(len(message))  # returns the number of characters in a string
    print(message[3])  # indexing returns char at that index value
    print(message[0:5])  # range based indexing is called slicing
    # & includes index 0 up to but not index 5
    # slicing from the beggining can also be written as [:5]
    # & to the end as [6:] == "World"
    print(message.lower())  # changes all chars to lower case
    print(message.upper())  # changes all chars to upper case
    print(message.count("o"))  # counts occurance of a char or str
    print(message.count("Hello"))
    print(message.find("World"))  # returns index of first char in str
    # find returns -1 if the str or char is not found in the var
    message = message.replace("World", "Universe")
    # replaces all occurances of str unless the count arg is put and
    # it will only replace that occurance. Default is all i.e. -1
    print(message)

    # STR FORMATTING
    # str formattin gis the best way to concatenate str instead of using +
    name = "Leslie"
    surname = "Musengi"
    greeting = "Hi {} {}. Welcome to the group!".format(name, surname)
    print(greeting)

    # F STRINGS
    # f strings are actually more interactive to use
    other_name = "Prudy"
    other_surname = "Musengi"
    # greeting_2 = f"Hi {other_name} {other_surname}. You have been added as well"
    # this is the syntax but somehow it is not working. Have to find out why


if __name__ == "__main__":
    main()
