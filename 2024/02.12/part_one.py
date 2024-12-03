# Updated script to handle space-separated integers
def count_safe_reports(reports):
    def is_safe(report):
        # Calculate differences between adjacent levels
        differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]        # Check if differences are within the range [1, 3] or [-3, -1]
        if not all(1 <= abs(diff) <= 3 for diff in differences):
            return False        # Check if the report is strictly increasing or decreasing
        if all(diff > 0 for diff in differences):
            return True  # Strictly increasing
        if all(diff < 0 for diff in differences):
            return True  # Strictly decreasing        return False  # Neither increasing nor decreasing    # Count the number of safe reports
    return sum(1 for report in reports if is_safe(report))
