from collections import defaultdict

class PrintQueueValidator:
    def __init__(self):
        self.dependencies = defaultdict(set)
        
    def add_rule(self, before, after):
        """Add a dependency rule: 'before' must be printed before 'after'"""
        self.dependencies[after].add(before)
        
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

def solve_print_queue(filename):
    """Main solution function"""
    # Parse input file
    rules, updates = parse_input_file(filename)
    
    # Initialize validator
    validator = PrintQueueValidator()
    
    # Add all rules
    for rule in rules:
        before, after = map(int, rule.split('|'))
        validator.add_rule(before, after)
    
    # Process updates and sum middle pages of valid sequences
    total = 0
    for update in updates:
        if validator.is_valid_order(update):
            middle_page = validator.get_middle_page(update)
            total += middle_page
    
    return total

# Run the solution
if __name__ == "__main__":
    result = solve_print_queue('input.txt')
    print(f"The sum of middle page numbers from valid updates is: {result}")