# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()

# running total of priorities
total_priority_sum = 0

# loop over all rucksacks in groups of threes
for sack in lines:
    # get middle index of sack
    mid = len(sack) // 2

    # split the sack into 2 partitions and convert to sets
    sackL = set(sack[:mid])
    sackR = set(sack[mid:])

    # find common elements amongst both sets
    common = sackL & sackR

    # running value of priorities for the current rucksack
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
