# IB CS pseudocode: loop COUNT from 1 to 5 ... end loop
# Python equivalent: for loop with range()

# range(1, 6) produces 1, 2, 3, 4, 5 (stop value is exclusive)
for count in range(1, 6):
    print("Count is:", count)

# range(start, stop, step) can count in any step size
print("\nCounting down by 2s:")
for count in range(10, 0, -2):
    print(count)

# Using a loop to build a running total (accumulator pattern)
total = 0
for number in range(1, 11):
    total = total + number

print("\nSum of numbers 1 to 10:", total)
