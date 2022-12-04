# Day 1 Part A - Solution

Simply run the script and view the terminal's output to view the answer. However, make sure that 
`FILE_MODE_REAL_INPUT_MODE` is set to true if you want to run the script against the problem input data the AOC challenge 
expects you to solve. Setting it to false will run the script against the contents of `test.txt` which is a 
test case presented in the problem itself. 

## Problem Difficulty (1-10)

3.5/10

## Solution Explanation

### Parsing Data

The main point of potential difficulty in this problem relies on parsing the text file and being 
familiar with the input/output libraries of your programming language of use. 

We simply use the `read().splitlines()` method to read the entire text contents of the file. Note that I use `splitlines()`
because it removes the `\n` character from every parsed line. 

So you know you have encountered an empty new line if you encounter the empty string `''` and not `\n`.
Hence, one thing that we need to be cautious of is that we know we are done counting calories for an elf once we reach
an empty string  `''` character, which is just a newline in the file. 

### Tracking Elf Data

This problem basically requires you to choose a suitable data structure like an array or dictionary, in this case we
use a dictionary, that is able to track the total calories that each elf is carrying with them.

I create a dictionary called `calories_dict` that works in the following manner; you can determine what the ith 
elf is carrying by simply accessing the dictionary in the following manner `calories_dict[i]`. We then update this
dictionary value as we parse through the input data.

### Processing Elf Data

We loop through all the data and each time we see an empty string we increment the `elf_index` variable
because we know we are done processing the current elf's total carrying calories. 

Otherwise, we simply convert the line into an integer and then check if there is an entry in `calories_dict` for the
current elf we are processing. If that key doesnt exist we simply create it and store the value of the calories and
if it does exist we just update the total sum for that elf, which is what occurs on **lines 25-28**.

### Finding Max Calories

Simply get all the values in the dictionary by calling `calories_dict.values()` and run the `max()` function on that
object to get the maximum number of calories any elf is carrying. 

## Answer

The answer for this problem is **68467** given my specialized input data noting that every AOC user will not receive the
same input data even for the same problem.
