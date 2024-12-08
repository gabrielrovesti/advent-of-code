from itertools import product

def parse_line(line):
    """Parse a line into test value and numbers"""
    test_value, numbers = line.split(':')
    return int(test_value), [int(x) for x in numbers.split()]

def evaluate_expression(numbers, operators):
    """Evaluate expression left to right using given operators"""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        else:  # op == '*'
            result *= numbers[i + 1]
    return result

def can_equation_be_true(test_value, numbers):
    """Check if any combination of operators can produce test value"""
    # Generate all possible combinations of + and * operators
    n_operators = len(numbers) - 1
    for ops in product(['+', '*'], repeat=n_operators):
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

def solve(filename):
    total = 0
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
                
            test_value, numbers = parse_line(line)
            if can_equation_be_true(test_value, numbers):
                total += test_value
                
    return total

if __name__ == "__main__":
    result = solve('input.txt')
    print(f"Total calibration result: {result}")