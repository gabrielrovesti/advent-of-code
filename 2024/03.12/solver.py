# import re

# def sum_of_multiplications(input_string):
#     pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
#     total = 0
    
#     for match in re.finditer(pattern, input_string):
#         x = int(match.group(1))
#         y = int(match.group(2))
#         total += x * y
    
#     return total

# # Read input from file
# with open('input.txt', 'r') as file:
#     input_data = file.read()

# result = sum_of_multiplications(input_data)
# print(f"The sum of all valid multiplications is: {result}")

# Solution: 192767529

import re

def sum_of_enabled_multiplications(input_string):
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    total = 0
    mul_enabled = True
    
    for match in re.finditer(f'{mul_pattern}|{do_pattern}|{dont_pattern}', input_string):
        if match.group(0).startswith('mul'):
            if mul_enabled:
                x = int(match.group(1))
                y = int(match.group(2))
                total += x * y
        elif match.group(0) == 'do()':
            mul_enabled = True
        else:  # 'don't()'
            mul_enabled = False
    
    return total

# Read input from file
with open('input.txt', 'r') as file:
    input_data = file.read()

result = sum_of_enabled_multiplications(input_data)
print(f"The sum of all enabled multiplications is: {result}")

# Solution: 104083373