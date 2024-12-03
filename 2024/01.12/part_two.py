### Part Two ###

from collections import Counter

with open('input.txt') as f:
    lines = f.readlines()

left_list = []
right_list = []
for line in lines:
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

# Count the occurrences of each number in the right list
right_counts = Counter(right_list)

similarity_score = 0
for num in left_list:
    count = right_counts[num]
    similarity_score += num * count

print(similarity_score)