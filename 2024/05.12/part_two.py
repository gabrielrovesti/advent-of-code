from collections import defaultdict, deque

class PrintQueueValidator:
    def __init__(self):
        self.dependencies = defaultdict(set)
        self.reverse_deps = defaultdict(set)
        
    def add_rule(self, before, after):
        """Add a dependency rule: 'before' must be printed before 'after'"""
        self.dependencies[after].add(before)
        self.reverse_deps[before].add(after)
        
    def is_valid_order(self, pages):
        """Check if a given order of pages satisfies all relevant dependencies"""
        pages_set = set(pages)
        
        for i, page in enumerate(pages):
            required_before = self.dependencies[page]
            relevant_deps = required_before.intersection(pages_set)
            pages_before = set(pages[:i])
            
            if not relevant_deps.issubset(pages_before):
                return False
                
        return True
    
    def get_middle_page(self, pages):
        """Find the middle page number in a sequence"""
        return pages[len(pages) // 2]
        
    def reorder_sequence(self, pages):
        """Reorder a sequence of pages according to dependency rules"""
        # Create graph for just the pages in this sequence
        pages_set = set(pages)
        in_degree = defaultdict(int)
        graph = defaultdict(set)
        
        # Build the graph using only relevant dependencies
        for page in pages_set:
            deps = self.dependencies[page].intersection(pages_set)
            for dep in deps:
                graph[dep].add(page)
                in_degree[page] += 1
                
        # Initialize queue with pages that have no dependencies
        queue = deque()
        for page in pages_set:
            if in_degree[page] == 0:
                queue.append(page)
                
        # Perform topological sort
        result = []
        while queue:
            current = queue.popleft()
            result.append(current)
            
            for next_page in graph[current]:
                in_degree[next_page] -= 1
                if in_degree[next_page] == 0:
                    queue.append(next_page)
                    
        return result

def parse_input_file(filename):
    """Parse the input file into rules and updates sections"""
    rules = []
    updates = []
    reading_rules = True
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                reading_rules = False
                continue
                
            if reading_rules:
                rules.append(line)
            else:
                updates.append([int(x) for x in line.split(',')])
    
    return rules, updates

def solve_print_queue_part2(filename):
    """Solution for part 2"""
    # Parse input file
    rules, updates = parse_input_file(filename)
    
    # Initialize validator
    validator = PrintQueueValidator()
    
    # Add all rules
    for rule in rules:
        before, after = map(int, rule.split('|'))
        validator.add_rule(before, after)
    
    # Process only invalid updates
    total = 0
    for update in updates:
        if not validator.is_valid_order(update):
            corrected_order = validator.reorder_sequence(update)
            middle_page = validator.get_middle_page(corrected_order)
            total += middle_page
    
    return total

# Run both parts
if __name__ == "__main__":
    result = solve_print_queue_part2('input.txt')
    print(f"The sum of middle page numbers from reordered invalid updates is: {result}")