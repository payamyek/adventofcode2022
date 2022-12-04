# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()

# running total of priorities
total_priority_sum = 0

# loop over all rucksacks in groups of threes
for i in range(0, len(lines) - 2, 3):
    # get the three related rucksacks
    sacks = [lines[i], lines[i+1], lines[i+2]]

    # find common elements among all three sets
    common = set(sacks[0]) & set(sacks[1]) & set(sacks[2])

    # running value of priorities for the current group rucksacks
    priority_sum = 0

    # compute priorities of each common element
    for c in common:
        # calculate priority of element by shifting their ascii values to fit the problem's specification
        if c.isupper():
            priority_sum += ord(c) - 38
        else:
            priority_sum += ord(c) - 96

    # update running total
    total_priority_sum += priority_sum

# print result to screen
print(total_priority_sum)
