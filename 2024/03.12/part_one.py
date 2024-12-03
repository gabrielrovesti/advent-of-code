import re
def sum_of_multiplications(input_string):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    total = 0
  
    for match in re.finditer(pattern, input_string):
        x = int(match.group(1))
        y = int(match.group(2))
        total += x * y
  
    return total
# Read input from file
with open('input.txt', 'r') as file:
    input_data = file.read()
result = sum_of_multiplications(input_data)
print(f"The sum of all valid multiplications is: {result}")

# Solution: 192767529
