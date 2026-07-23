# Nested loops: a loop inside another loop.
# The inner loop completes all of its iterations for every single
# iteration of the outer loop.

# Example: print a multiplication table from 1x1 to 5x5
for row in range(1, 6):
    line = ""
    for col in range(1, 6):
        product = row * col
        line = line + str(product).rjust(4)
    print(line)

# Example: 2D grid processing (common in IB CS for arrays/tables)
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nGrid contents:")
for row in grid:
    for value in row:
        print(value, end=" ")
    print()  # newline after each row

# Example: nested loop with a total across a 2D structure
total = 0
for row in grid:
    for value in row:
        total = total + value

print("\nSum of all values in grid:", total)
