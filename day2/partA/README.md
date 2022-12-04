# Day 2 Part A - Solution

This problem is what I call a "brute force party" as it requires you to essentially brute force all the possible
moves the players could make and then determine the result of such actions. Since rock, paper, scissors (RPS)
is a simple game with a small amount of possible combinations, brute forcing is a viable and actually desired approach. 

Simply run the script and view the terminal's output to view the answer. However, make sure that 
`FILE_MODE_REAL_INPUT_MODE` is set to true if you want to run the script against the problem input data the AOC challenge 
expects you to solve. Setting it to false will run the script against the contents of `test.txt` which is a 
test case presented in the problem itself. 

## Problem Difficulty (1-10)

4/10

## Solution Explanation

### Parsing Input Data

The input file consists of two characters seperated by a space on separate lines. We can simply just read in this data 
and utilize the `split()` function to extract the player moves in the following manner 
`'A Y'.split(" ") == ['A', 'Y']`. Notice that we commonly utilize the function `strip()` which just removes the `\n`
character from each line.

This extraction is at the heart of the problem because once we have the player moves we simply just hae to write the 
brute force logic to calculate the total points each move grants player two.

### Calculate Points

To calculate the number of points player two receives after each move we just have to brute force all the possible 
combinations that can occur in a game of RPS. 

As long as you read the question properly, determining the number of points player two receives for each move
combination is a relatively simple task.

## Answer

The answer for this problem is **10595**.

This answer is true for my given specialized input data. Note that every AOC user will not receive the
same input data for even the same problem.