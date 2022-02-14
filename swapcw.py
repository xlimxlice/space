from curses.ascii import isupper


def swap(old_string):
    newString = ''

    for character in old_string:
        if character.isupper():
            newString = newString + character.lower()
        elif character.islower():
            newString = newString + character.upper()
        else:
            newString = newString + character
    print(newString)

swap("VaLenTine is On tHE 14th, yEaRly. i aM bAe's bOO")