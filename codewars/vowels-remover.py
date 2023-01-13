def remove_vowel(string):

    vowels = ("a", "e", "i", "o", "u")

    if string.isalpha() and string.isupper():
        return string


print(remove_vowel("HELLOOO"))
