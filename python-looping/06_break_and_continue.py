# break  -> exits the loop immediately, skipping any remaining iterations
# continue -> skips the rest of the current iteration and moves to the next one

numbers = [3, 7, 2, 9, 4, 12, 5, 8]

# break: stop searching as soon as the target is found
target = 9
print("Searching for", target)
for number in numbers:
    if number == target:
        print("Found it! Stopping the search.")
        break
    print("Checked:", number)

# continue: skip even numbers, only print odd numbers
print("\nOdd numbers only:")
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

# break used inside a while loop to search for the first value over 10
print("\nFirst value greater than 10:")
index = 0
while index < len(numbers):
    if numbers[index] > 10:
        print(numbers[index])
        break
    index = index + 1
