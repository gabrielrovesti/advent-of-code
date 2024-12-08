def get_next_pos(pos, dir):
    """Calculate next position based on direction."""
    DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left
    return (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])

def is_valid_pos(pos, grid):
    """Check if position is within grid bounds."""
    return 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0])

def simulate_path(grid, x, y, dir, blocked_pos=None):
    """Simulates the guard's path and returns if it creates a loop."""
    seen_states = set()
    current_pos = (x, y)
    steps = 0
    max_steps = len(grid) * len(grid[0]) * 4  # Maximum possible states
    
    while steps < max_steps:
        # Exit if we're out of bounds
        if not is_valid_pos(current_pos, grid):
            return False
            
        # Check for loop
        state = (current_pos[0], current_pos[1], dir)
        if state in seen_states:
            return True
        seen_states.add(state)
        
        # Calculate next position
        next_pos = get_next_pos(current_pos, dir)
        
        # Check if we hit an obstacle or go out of bounds
        hits_obstacle = (
            not is_valid_pos(next_pos, grid) or
            (is_valid_pos(next_pos, grid) and grid[next_pos[1]][next_pos[0]] == '#') or
            next_pos == blocked_pos
        )
        
        if hits_obstacle:
            # Turn right
            dir = (dir + 1) % 4
        else:
            # Move forward
            current_pos = next_pos
            
        steps += 1
    
    return True  # If we hit max steps, probably in a loop

def find_start(grid):
    """Find starting position and direction of guard."""
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '^':
                return (x, y)
    return None

def solve(filename):
    """Find number of positions that create loops."""
    # Read and parse input
    with open(filename) as f:
        grid = [list(line.strip()) for line in f]
    
    # Find start position
    start_pos = find_start(grid)
    if not start_pos:
        return 0
    
    # Try each empty position as an obstacle
    loop_count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            # Only try empty spaces that aren't the start position
            if grid[y][x] == '.' and (x, y) != start_pos:
                if simulate_path(grid, start_pos[0], start_pos[1], 0, (x, y)):
                    loop_count += 1
    
    return loop_count

if __name__ == "__main__":
    result = solve('input.txt')
    print(f"Number of positions that create loops: {result}")