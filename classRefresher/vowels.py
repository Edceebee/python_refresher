def vowels():
    name = input("Enter name: ")
    for letters in name:
        if letters in ("a", "e", "i", "o", "u"):
            print(letters, "is vowel")

        else:
            print(letters, "is not vowel")


vowels()