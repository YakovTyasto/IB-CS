# Two common IB CS loop patterns:
# 1. Sentinel-controlled loop: keep looping until a special "sentinel"
#    value is reached (often used to simulate reading input until
#    a stop marker appears).
# 2. Accumulator pattern: build up a total, count, or list across
#    the iterations of a loop.

# Sentinel-controlled loop: -1 marks the end of the data
scores = [85, 92, 78, 60, -1]

index = 0
score = scores[index]

while score != -1:
    print("Processing score:", score)
    index = index + 1
    score = scores[index]

print("Sentinel value reached, loop stopped.")

# Accumulator pattern: total, count, and average
scores = [85, 92, 78, 60, 74]

total = 0
count = 0

for score in scores:
    total = total + score
    count = count + 1

average = total / count
print(f"\nTotal: {total}, Count: {count}, Average: {average}")

# Accumulator pattern building a new list (e.g. only passing grades)
passing_scores = []
for score in scores:
    if score >= 70:
        passing_scores.append(score)

print("Passing scores:", passing_scores)
