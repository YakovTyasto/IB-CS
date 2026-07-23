# IB CS pseudocode: loop WHILE condition ... end loop
# The while loop is condition-controlled: it checks the condition
# BEFORE running the loop body, so it may run zero times.

count = 1
while count <= 5:
    print("Count is:", count)
    count = count + 1

# Example: keep asking until the user enters a valid password
# (simulated here with a preset list instead of real input())
attempts = ["wrong1", "wrong2", "letmein"]
correct_password = "letmein"
index = 0
guess = ""

while guess != correct_password:
    guess = attempts[index]
    index = index + 1
    print("Trying password:", guess)

print("Access granted!")
