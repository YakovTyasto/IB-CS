# IB CS pseudocode: loop item in COLLECTION ... end loop
# Python equivalent: for loop iterating directly over a list

subjects = ["Maths", "Physics", "Computer Science", "English"]

for subject in subjects:
    print("Subject:", subject)

# Use enumerate() when both the index and the value are needed
print("\nWith index numbers:")
for index, subject in enumerate(subjects):
    print(index + 1, "-", subject)

# Looping over a string is also possible, since a string is a
# sequence of characters
word = "LOOP"
print("\nCharacters in the word:")
for letter in word:
    print(letter)
