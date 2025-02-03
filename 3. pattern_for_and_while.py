# 3. A program that will display the following given output. (for a. use nested for statement and for b. use nested while statement)

#a.
print("Output A:\n")
def pattern_a(n=5):
    for i in range(1, n + 1):
        print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))
pattern_a()

#b.
print("\nOutput B:\n")
def pattern_b():
    row = 1
    sequence = [1, 3, 5, 6, 7]  # Tha sequence of numbers for each row
    while row <= 5:
        num = sequence[row - 1] # Get the current number from the sequence
        count = 0 # Print number from the sequence in required reps
        while count < num:
            print(num, end="")
            count += 1

        spaces = 5 - row # Print leading spaces
        while spaces > 0:
            print(" ", end="")
            spaces -= 1
        
        print()  # Newline after each row
        row += 1
pattern_b()
