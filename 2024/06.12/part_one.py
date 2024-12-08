def count_visited_positions(grid):
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = None, None
    direction = None

    # Find the starting position and facing direction of the guard
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                start_row, start_col = i, j
                direction = (-1, 0)
            elif grid[i][j] == '>':
                start_row, start_col = i, j
                direction = (0, 1)
            elif grid[i][j] == 'v':
                start_row, start_col = i, j
                direction = (1, 0)
            elif grid[i][j] == '<':
                start_row, start_col = i, j
                direction = (0, -1)

    visited = set()
    curr_row, curr_col = start_row, start_col

    while 0 <= curr_row < rows and 0 <= curr_col < cols:
        visited.add((curr_row, curr_col))

        next_row, next_col = curr_row + direction[0], curr_col + direction[1]

        if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == '#':
            # Turn right
            direction = (direction[1], -direction[0])
        else:
            # Move forward
            curr_row, curr_col = next_row, next_col

    return len(visited)

# Read the input grid from the file
with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

# Count the number of distinct positions visited by the guard
result = count_visited_positions(grid)
print(result)