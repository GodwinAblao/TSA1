# 1. A program that will display the number of vowels, consonants, spaces, and other characters given an input string. (use for loop and some operators under module 1 and 2)

def count_characters(input_string):
    vowels = consonants = spaces = others = 0
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    
    for char in input_string:
        if char.isalpha():
            if char.lower() in vowels_set:
                vowels += 1
            else:
                consonants += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1

    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Spaces: {spaces}")
    print(f"Other characters: {others}")

# Get user input
input_string = input("Enter a string: ")
count_characters(input_string)


