# Day 5 Part A - Solution

Two-dimensional structures are hard to parse if you are not familiar with such structures. Therefore, the problem's 
main point of contention is the tricky format of the input data and the fact that the common place `split()` function is 
deemed useless in this scenario.


Simply run the script and view the terminal's output to view the answer. However, make sure that 
`FILE_MODE_REAL_INPUT_MODE` is set to true if you want to run the script against the problem input data the AOC challenge 
expects you to solve. Setting it to false will run the script against the contents of `test.txt` which is a 
test case presented in the problem itself. 

## Problem Difficulty (1-10)

6/10

## Solution Explanation

### Parsing Stack Data

We notice a pattern in the data and exploit this to extract the location of the crates with respect to the stacks.

Notice that every fourth character on a line is either a `[`, if a crate exists, otherwise empty. So we 
know a crate exists if a multiple of four index into the row is a `[`. For example, check the following indices for the 
character `[`: `0, 4, 8, 12, ...` and so on.

Then we know which stack the found crate belongs to by keeping track of its location using the variable `stack_index`
which simply stores how many times we incremented by four which is indeed the location of the crate.

We keep traversing the lines of the file until we hit a line that doesn't contain the `[`, which means
we hit a row that doesn't contain any crates and hence are done with processing the stacks and crates.

Note on **lines 47-48** we have to reverse the order of all the stacks because list structures in Python always require
us to add crates add the end of list which inverts the order of the crates and hence requires us to reverse its order.

### Parsing Moves

We simply use the regex library in Python to extract the move data and then we move the crates as accordance to those
instructions.

Using `pop()` removes the last element of a list, and we utilize this method here to perform these crate movements.

## Answer

The answer for this problem is *VGBBJCRMN*.

This answer is true for my given specialized input data. Note that every AOC user will not receive the
same input data for even the same problem.