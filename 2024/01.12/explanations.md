First, we need to read in the puzzle input and parse it into two lists of numbers. It looks like the numbers are given in two columns, so we can split each line on whitespace and convert the resulting strings to integers.

Here's how we can do that in Python:

```python
with open('input.txt') as f:
    lines = f.readlines()

left_list = []
right_list = []
for line in lines:
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))
```

This gives us two lists, `left_list` and `right_list`, containing the numbers from the left and right columns respectively.

Next, we need to pair up the numbers from smallest to largest in each list. We can do this by sorting both lists:

```python
left_list.sort()
right_list.sort()
```

Now that the lists are sorted, we can pair up the numbers at each index and calculate the distance between them. We'll keep a running total of the distances:

```python
total_distance = 0
for left, right in zip(left_list, right_list):
    distance = abs(left - right)
    total_distance += distance
```

Here we use `zip` to pair up the elements from `left_list` and `right_list`. For each pair, we calculate the absolute difference between the numbers using `abs(left - right)`, and add that distance to our `total_distance`.

After the loop finishes, `total_distance` will contain the sum of all the distances between the paired numbers.

This script will read the input from a file called `input.txt` (make sure to replace that with the path to your actual input file), calculate the total distance between the paired numbers, and print out the result.

---

Now, let's solve part two of this puzzle! We'll modify our previous solution to calculate the similarity score between the two lists.

Here's how it works:

1. We start by reading the input file and parsing the numbers into `left_list` and `right_list` as before.

2. Instead of sorting the lists, we use a `Counter` from the `collections` module to count the occurrences of each number in the right list. This gives us a dictionary `right_counts` where the keys are the numbers and the values are the counts.

3. We initialize a variable `similarity_score` to keep track of the running total.

4. We loop through each number `num` in the left list:
   - We look up the count of `num` in the right list using `right_counts[num]`. If `num` doesn't appear in the right list, this will default to 0.
   - We multiply `num` by its count and add the result to `similarity_score`.

5. After the loop finishes, `similarity_score` will contain the total similarity score between the left and right lists.

6. Finally, we print out the similarity score.

To use this script, make sure to replace `'input.txt'` with the path to your actual input file.
