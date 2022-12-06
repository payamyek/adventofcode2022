import re

# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()

# index to track which rows from the file have been processed
row_index = 0

# data structure representing our stacks
stacks = dict()

# process the stacks structure
for line in lines:

    # stop processing the crates once no crates found
    if '[' not in line:
        break

    # the stack the crate belongs to
    stack_index = 1

    # extract all crates from row
    for i in range(0, len(line) - 2, 4):

        # valid crate
        if line[i] == '[':
            # extract crate
            crate = line[i:i+3]

            # create list if stack not already initialized
            if stacks.get(stack_index) is None:
                stacks[stack_index] = [crate]
            else:
                stacks[stack_index].append(crate)

        stack_index += 1
    row_index += 1

# reverse all the crates
for key in stacks:
   stacks[key].reverse()

# process moves
for move in lines[row_index+2:]:
    # regex to extract move data
    result = re.search("move (\d+) from (\d+) to (\d+)", move)

    # extract move data
    quantity, stack_source, stack_dest = int(result.group(1)), int(result.group(2)), int(result.group(3))

    # track all crates that need to be moved
    crates_to_move = []
    for _ in range(quantity):
        # crate to be moved
        crates_to_move.append(stacks[stack_source].pop())

    # reverse to maintain original order of the crates
    crates_to_move.reverse()

    # move the crates
    stacks[stack_dest] += crates_to_move


# get all stack keys
keys = list(stacks.keys())
keys.sort()

# store result
result = ''

# get all top crates from each stack
for key in keys:
    result += stacks[key].pop().removeprefix("[").removesuffix("]")

# print result
print(result)

