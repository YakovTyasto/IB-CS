# IB CS pseudocode: loop ... until condition end loop
# This is a REPEAT-UNTIL loop: the body always runs at least once,
# and the condition is checked AFTER the body (post-condition loop).
# Python has no built-in repeat-until, so it is built from
# while True combined with a break.

number = 0

while True:
    number = number + 1
    print("Number is:", number)

    if number >= 5:   # equivalent to "until number >= 5"
        break

print("Loop finished because number reached", number)

# Example: simulate rolling a die until a 6 is rolled
import random

rolls = 0
while True:
    roll = random.randint(1, 6)
    rolls = rolls + 1
    print("Rolled:", roll)

    if roll == 6:
        break

print(f"\nIt took {rolls} roll(s) to get a 6")
