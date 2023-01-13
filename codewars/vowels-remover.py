def remove_vowel(string):

    vowels = ("a", "e", "i", "o", "u")

    if string.isalpha() and string.isupper():
        return string
    elif string.isalpha() and string.islower():
        for letter in string:
            if letter in vowels:
                string = string.replace(letter, "")
        return string
    else:
        for letter in string:
            if letter in vowels:
                string = string.replace(letter, "")
        return string


print(remove_vowel("HELLOOO"))
print(remove_vowel("apple"))
print(remove_vowel("sajeet"))
print(remove_vowel("I loVe PytHOn"))
print(remove_vowel("jAvaScript Is Also grEat"))
print(remove_vowel("fooo fOOOo"))
