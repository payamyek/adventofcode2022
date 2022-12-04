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

    value = int(line)  # remove newlines and convert to int

    # store running total of the elf's total calorie count
    if calories_dict.get(elf_index) is None:
        calories_dict[elf_index] = value
    else:
        calories_dict[elf_index] += value


# convert dictionary values to list
calories_list = list(calories_dict.values())

# first largest value
max_calories_one = max(calories_list)

# remove largest value from list
calories_list = list(filter(lambda val: (val != max_calories_one), calories_list))

# second largest value
max_calories_two = max(calories_list)

# remove second largest value from list
calories_list = list(filter(lambda val: (val != max_calories_two), calories_list))

# third largest value
max_calories_three = max(calories_list)

# print result
print(max_calories_one + max_calories_two + max_calories_three)
