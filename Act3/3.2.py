first_name = str(input("Enter First name: "))
last_name =str(input("Enter Last name: "))

# Concatenate to form full name
full_name = first_name + " " + last_name


# Display the results
print("Full Name:", full_name)
print("Full Name (Upper case):", full_name.upper())
print("Full Name (Lower case):", full_name.lower())

full_name_length = len(full_name.replace(" ", ""))
print("Length of Full Name:", full_name_length)