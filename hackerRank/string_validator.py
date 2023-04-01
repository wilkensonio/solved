if __name__ == '__main__':
    s = input()

    if any(letter.isalnum() for letter in s):
        print(True)
    else:
        print(False)
    if any(letter.isalpha() for letter in s):
        print(True)
    else:
        print(False)
    if any(letter.isdigit() for letter in s):
        print(True)
    else:
        print(False)
    if any(letter.islower() for letter in s):
        print(True)
    else:
        print(False)
    if any(letter.isupper() for letter in s):
        print(True)
    else:
        print(False)
