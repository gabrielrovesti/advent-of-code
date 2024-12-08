def simulate_guard_movement(grid, start_pos, start_dir):
    """Simulates the guard's movement and returns the set of visited positions."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
    pos = start_pos
    dir_idx = start_dir
    visited = set([pos])

    while True:
        next_pos = (pos[0] + directions[dir_idx][0], pos[1] + directions[dir_idx][1])
        if grid[next_pos[0]][next_pos[1]] == '#':
            dir_idx = (dir_idx + 1) % 4
            # Print the invalid coordinates for debugging
            print(f"Invalid position accessed: {next_pos}")
        else:
            pos = next_pos
            visited.add(pos)
            if pos not in grid:
                break

    return visited

def find_loop_positions(grid, start_pos, start_dir):
    """Finds positions for a new obstruction to create a loop."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pos = start_pos
    dir_idx = start_dir
    loop_positions = set()

    def check_loop(pos, dir_idx):
        next_pos = (pos[0] + directions[dir_idx][0], pos[1] + directions[dir_idx][1])
        if grid[next_pos[0]][next_pos[1]] == '#':
            return False
        if next_pos in loop_positions:
            return True
        loop_positions.add(next_pos)
        return check_loop(next_pos, dir_idx)

    while True:
        next_pos = (pos[0] + directions[dir_idx][0], pos[1] + directions[dir_idx][1])
        if grid[next_pos[0]][next_pos[1]] == '#':
            dir_idx = (dir_idx + 1) % 4
        else:
            pos = next_pos
            if check_loop(pos, dir_idx):
                loop_positions.remove(pos)  # Remove the current position as it's not a valid loop start
            if pos not in grid:
                break

    return loop_positions

# Read the input from the file
with open("input.txt", "r") as f:
    grid = {}
    y = 0
    for line in f:
        for x, char in enumerate(line.strip()):
            grid[(x, y)] = char
        y += 1

# Find the starting position and direction
for pos, char in grid.items():
    if char == '^':
        start_pos = pos
        start_dir = 0  # Up

# Part 1: Count the number of visited positions
visited_positions = simulate_guard_movement(grid, start_pos, start_dir)
print("Part 1:", len(visited_positions))

# Part 2: Find loop positions
loop_positions = find_loop_positions(grid, start_pos, start_dir)
print("Part 2:", len(loop_positions))