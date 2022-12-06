# Day 5 Part B - Solution

The solution to this problem is an one-line statement if you have properly implemented the first part. 

Simply run the script and view the terminal's output to view the answer. However, make sure that 
`FILE_MODE_REAL_INPUT_MODE` is set to true if you want to run the script against the problem input data the AOC challenge 
expects you to solve. Setting it to false will run the script against the contents of `test.txt` which is a 
test case presented in the problem itself. 

## Problem Difficulty (1-10)

0.5/10

## Solution Explanation

### Parsing Stack Data (Same as Part A)

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

### Parsing Moves (Same as Part A)

We simply use the regex library in Python to extract the move data, and then we move the crates as accordance to those
instructions.

There isn't really much to explain here other than that you must be familiar with basic regex expressions in order
to effectively parse the moves. Other solutions exist but using regex is the most natural solution in my opinion. 

### Performing the Crate Moves

Using `pop()` removes the last element of a list, and we exactly utilize this method here to perform the crate movements.

So if the instruction is `move 2 from 3 to 1`, we do the following:

1. Access the third stack using `stacks[3]`
2. Remove two items from `stacks[3]` by calling `pop()` twice and store the popped crates into a local variable
3. **Reverse the order of the popped crates to adhere to the new rules**  (THAT'S IT)
4. Access the first stack using `stacks[1]`
5. Update the first stack by adding the newly popped crates to the first stack


## Answer

The answer for this problem is *LBBVJBRMH*.

This answer is true for my given specialized input data. Note that every AOC user will not receive the
same input data for even the same problem.