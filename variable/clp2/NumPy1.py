import random 
matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
print("Generated 5x5 Matrix:")
for row in matrix:
    print(row)
row_sums = [sum(row) for row in matrix]
print("\nRow-wise Sums:")
for i, total in enumerate(row_sums):
    print(f"Row {i + 1}: {total}")
