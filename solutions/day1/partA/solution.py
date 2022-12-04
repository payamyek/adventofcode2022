# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

calories_dict = dict()  # stores the number of calories the ith elf is carrying
elf_index = 1  # loop counter

# open file  for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()

# calculate total calories carried by each elf
for line in lines:

    # found new line, so we start processing calorie data for next elf and skip rest of statements
    if line == '':
        elf_index += 1
        continue

    value = int(line)  # convert to int

    # store running total of the elf's total calorie count
    if calories_dict.get(elf_index) is None:
        calories_dict[elf_index] = value
    else:
        calories_dict[elf_index] += value


# find max calories that can be carried by one elf
max_calories = max(calories_dict.values())

# print result
print(max_calories)
