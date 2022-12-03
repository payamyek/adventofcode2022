# Day 1 Part B - Solution

Code remains the same for majority of the file, changes can be found after **line 32.**

Simply run the script and view the terminals output to view the answer. However, make sure that 
`FILE_MODE_REAL_INPUT_MODE` is set to true if you want to run the script against the problem input data the AOC challenge 
expects you to solve. Setting it to false will run the script against the contents of `test.txt` which is a 
test case presented in the problem itself. 

## Problem Difficulty (1-10)

1/10

## Problem Methodology

This problem is relatively easy if you have properly solved part A of the problem set.

Simply, convert the dictionary's values into a list.

Then find the largest value in the list and remove all occurrences of it.

Then find the largest value of the new list, which is now the global second largest value, and remove all occurrences 
of it from the list.

Finally, we find the largest value of the new list which is now the global third largest value.

We sum these three values and get our desired answer. 

## Answer

The answer for this problem is **203420** given my specialized input data noting that every AOC user will not receive the
same input data even for the same problem.