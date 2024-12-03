### Part two ###

def count_safe_reports(reports):
    def is_safe(report):
        # Calculate differences between adjacent levels
        differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

        # Check if differences are within the range [1, 3] or [-3, -1]
        if not all(1 <= abs(diff) <= 3 for diff in differences):
            return False

        # Check if the report is strictly increasing or decreasing
        if all(diff > 0 for diff in differences):
            return True  # Strictly increasing
        if all(diff < 0 for diff in differences):
            return True  # Strictly decreasing

        return False  # Neither increasing nor decreasing

    def is_safe_with_dampener(report):
        # If the report is already safe, return True
        if is_safe(report):
            return True

        # Try removing each level and check if the resulting report is safe
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                return True

        return False

    # Count the number of safe reports using the dampener logic
    return sum(1 for report in reports if is_safe_with_dampener(report))

# Read the reports from the input file
reports = []
with open('input.txt') as f:
    for line in f:
        # Parse integers from space-separated values in each line
        numbers = list(map(int, line.split()))
        if numbers:  # Ensure the line isn't empty
            reports.append(numbers)
# Count and print the number of safe reports
safe_count = count_safe_reports(reports)
print(f"Number of safe reports: {safe_count}")