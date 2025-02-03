#2. A program that will count the sum of the digits from a given input string digits. (use for loop and some operators under module 1 and 2)

def sum_of_digits(input_string):
    total = 0
    for char in input_string:
        if char.isdigit():
            total += int(char)
    
    print(f"Sum of digits: {total}")

# Get user input
input_string = input("Enter a string with digits: ")
sum_of_digits(input_string)
