def parse_grid(filename):
    """Parse input file into a grid and collect antenna positions by frequency"""
    grid = []
    antennas = {}  # frequency -> list of (x,y) positions
    
    with open(filename, 'r') as f:
        for y, line in enumerate(f):
            row = list(line.strip())
            grid.append(row)
            
            # Collect antenna positions
            for x, char in enumerate(row):
                if char != '.':
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((x, y))
                    
    return grid, antennas

def find_antinodes(grid, antennas):
    """Find all unique antinode positions"""
    height = len(grid)
    width = len(grid[0])
    antinodes = set()
    
    # For each frequency, check all pairs of antennas
    for freq, positions in antennas.items():
        for i, pos1 in enumerate(positions):
            x1, y1 = pos1
            for j, pos2 in enumerate(positions[i+1:], i+1):
                x2, y2 = pos2
                
                # Check if antennas are in same row or column (collinear requirement)
                if x1 == x2:  # Same column
                    # Calculate potential antinode y-positions
                    dy = y2 - y1
                    # One antinode point would be 1/3 of the way from antenna1 to antenna2
                    y3 = y1 + dy // 3
                    # The other would be 2/3 of the way
                    y4 = y1 + (2 * dy) // 3
                    
                    # Add antinodes if they're within bounds
                    if 0 <= y3 < height:
                        antinodes.add((x1, y3))
                    if 0 <= y4 < height:
                        antinodes.add((x1, y4))
                        
                elif y1 == y2:  # Same row
                    # Calculate potential antinode x-positions
                    dx = x2 - x1
                    # One antinode point would be 1/3 of the way from antenna1 to antenna2
                    x3 = x1 + dx // 3
                    # The other would be 2/3 of the way
                    x4 = x1 + (2 * dx) // 3
                    
                    # Add antinodes if they're within bounds
                    if 0 <= x3 < width:
                        antinodes.add((x3, y1))
                    if 0 <= x4 < width:
                        antinodes.add((x4, y1))
    
    return antinodes

def solve(filename):
    # Parse input
    grid, antennas = parse_grid(filename)
    
    # Find antinodes
    antinodes = find_antinodes(grid, antennas)
    
    # Print result
    print(f"Found {len(antinodes)} unique antinode positions")
    return len(antinodes)

if __name__ == "__main__":
    answer = solve('input.txt')
    print(f"Answer: {answer}")