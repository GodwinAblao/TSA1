# Asking the user for the first and last term numbers
first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))

# Calculating the sum of numbers from first term to last term (inclusive)
sum_of_terms = sum(range(first_term, last_term + 1))

# Displaying the result
print(f"The sum of the numbers from {first_term} to {last_term} is {sum_of_terms}")
