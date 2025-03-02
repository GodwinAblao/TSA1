# Define sets based on the given Venn diagram
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# (a) How many elements are there in set A and B (union of A and B)
elements_in_A_and_B = A | B  # Union of A and B
print("Elements in A and B:", elements_in_A_and_B)
print("Count:", len(elements_in_A_and_B))

# (b) How many elements are there in B that is not part of A and C
elements_in_B_not_A_or_C = B - (A | C)  # Elements in B but not in A or C
print("Elements in B but not in A or C:", elements_in_B_not_A_or_C)
print("Count:", len(elements_in_B_not_A_or_C))

# (c) Show the following using set operations:

# (i) [h, i, j, k] → Elements in C but not in A or B
result_i = C - (A | B)
print("i. Elements in C but not in A or B:", result_i)

# (ii) [c, d, f] → Intersection of all three sets (A ∩ B ∩ C)
result_ii = A & B & C
print("ii. Intersection of A, B, and C:", result_ii)

# (iii) [b, c, h] → Elements in A ∩ B or B ∩ C
result_iii = (A & B) | (B & C)
print("iii. Elements in A ∩ B or B ∩ C:", result_iii)

# (iv) [d, f] → Elements in A ∩ C but not in B
result_iv = (A & C) - B
print("iv. Elements in A ∩ C but not in B:", result_iv)

# (v) [c] → Element present in all three sets
result_v = A & B & C
print("v. Element present in A, B, and C:", result_v)

# (vi) [l, m, o] → Elements unique to B
result_vi = B - (A | C)
print("vi. Elements unique to B:", result_vi)