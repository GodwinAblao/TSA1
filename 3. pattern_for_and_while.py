# 3. A program that will display the following given output. (for a. use nested for statement and for b. use nested while statement)

#a.
def pattern_a(n=5):
    for i in range(1, n + 1):
        print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))

pattern_a()

#b.
def pattern_b():
    i = 1
    while i <= 7:
        if i % 2 == 1:  # Print only for odd numbers
            print(str(i) * i)
        i += 1

pattern_b()
