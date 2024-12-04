def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Define all possible directions to search
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # diagonal down-right
        (-1, 1),  # diagonal up-right
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1), # diagonal up-left
        (1, -1)   # diagonal down-left
    ]
    
    def check_direction(row, col, dx, dy):
        if (row + 3*dx < 0 or row + 3*dx >= rows or 
            col + 3*dy < 0 or col + 3*dy >= cols):
            return False
        
        return (grid[row][col] == 'X' and 
                grid[row + dx][col + dy] == 'M' and
                grid[row + 2*dx][col + 2*dy] == 'A' and
                grid[row + 3*dx][col + 3*dy] == 'S')
    
    # Check each starting position
    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                if check_direction(row, col, dx, dy):
                    count += 1
    
    return count

# Read input from file
with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

result = find_xmas(grid)
print(f"XMAS appears {result} times in the word search")