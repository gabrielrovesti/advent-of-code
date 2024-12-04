def find_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def check_mas(row, col, dx, dy):
        # Check if MAS pattern exists in given direction
        # Returns True for both MAS and SAM
        if (row + 2*dx < 0 or row + 2*dx >= rows or 
            col + 2*dy < 0 or col + 2*dy >= cols):
            return False
            
        chars = [
            grid[row][col],
            grid[row + dx][col + dy],
            grid[row + 2*dx][col + 2*dy]
        ]
        return (chars == ['M', 'A', 'S'] or chars == ['S', 'A', 'M'])
    
    # Check each potential center position (the 'A' position)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # Center must be 'A'
            if grid[row][col] != 'A':
                continue
                
            # Check if we have a valid X-MAS pattern
            # One MAS/SAM must go from top-left to bottom-right
            # The other must go from top-right to bottom-left
            if ((check_mas(row - 1, col - 1, 1, 1) and 
                 check_mas(row - 1, col + 1, 1, -1)) or
                (check_mas(row + 1, col + 1, -1, -1) and 
                 check_mas(row + 1, col - 1, -1, 1))):
                count += 1
    
    return count

# Read input from file
with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

result = find_x_mas(grid)
print(f"X-MAS appears {result} times in the word search")