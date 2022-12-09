# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()

def get_parent(path):
    if path.count('/') == 1:
        return '/'

    index = path[:len(path) - 1].rindex('/')
    return path[:index + 1]

def safe_dict_update (dict_obj, key, value):
    if dict_obj.get(key) is None:
        directory_dict[key] = value
    else:
        directory_dict[key] += value


# store absolute paths for all files
files_dict = dict()

# current working directory
cwd = ''

# process file input
for line in lines:
    tokens = line.split(' ')

    if '$' in line and 'cd' in line and tokens[2] == '/':
        cwd = '/'
    elif '$' in line and 'cd' in line and tokens[2] == '..':
        cwd = get_parent(cwd)
    elif '$' in line and 'cd' in line:
        cwd = f"{cwd}{tokens[2]}/"
    elif '$' not in line and 'dir' not in line:
        file_path = f"{cwd}{tokens[1]}"
        files_dict[file_path] = int(tokens[0])

# store total size of each dict
directory_dict = dict()

def cascade_size_changes(path_name, size):
    parent_path = get_parent(path_name)

    while parent_path != '/':
        safe_dict_update(directory_dict, parent_path, size)
        parent_path = get_parent(parent_path)

    # update root directory size
    safe_dict_update(directory_dict, '/', size)

# calculate sizes of each directory
for k, v in files_dict.items():
    cascade_size_changes(k, v)

result = 0

#
for v in directory_dict.values():
    if v <= 100000:
        result += v


print (result)