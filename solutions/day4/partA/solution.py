# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()
    lines = [line.split(',') for line in lines]

# parse data into tuples of arrays
sections = [(x.split("-"), y.split("-")) for x, y in lines]

# running total
total_sum = 0

for x, y in sections:
    # get range start and endpoints for first pair
    x1, x2 = int(x[0]), int(x[1])

    # get range start and endpoints for second pair
    y1, y2 = int(y[0]), int(y[1])

    # check if either range of sections is a subset of the other
    if y1 <= x1 <= x2 <= y2 or x1 <= y1 <= y2 <= x2:
        total_sum += 1

# print result
print(total_sum)
