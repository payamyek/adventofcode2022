# Day 3 Part B - Solution

This problem mainly relies on your ability to find the intersection of two sets and simple string manipulation. 

Simply run the script and view the terminal's output to view the answer. However, make sure that 
`FILE_MODE_REAL_INPUT_MODE` is set to true if you want to run the script against the problem input data the AOC challenge 
expects you to solve. Setting it to false will run the script against the contents of `test.txt` which is a 
test case presented in the problem itself. 

## Problem Difficulty (1-10)

3/10

## Solution Explanation

### Splitting String into Two Equal Partitions

This part simply relies on your ability to perform simple string manipulation. 

Since we know that "A given rucksack always has the same number of items in each of its two compartments", we are 
guaranteed that the total length of a rucksack is even and hence `len(rucksack)//2` is exactly the middle of the two
partitions. 

Note, we need to use integer division in this case because otherwise the result would be a float and we cant
use float indices to manipulate lists. 

We then simply split the string into two smaller strings by storing the first half and second half of the rucksack 
into different variables `sackL, sackR`.

### Finding Common Elements

This problem boils down to your understanding of set operations. 

We can easily find common elements amongst sets by simply taking their intersections. 

However, note that each rucksack is represented by a string. However, in python we can convert a string easily into a 
set of its characters through the following operation: `set('abC') == {'a','b','C'}`.

This is important because we now have a set of characters, remember that sets are unordered and duplicates aren't allowed, 
which allows us to use a special operation know as intersection. 

Once we have the two sets: `sackL, sackR = {'a','b','c'}, {'a'}`.
We can find their intersection, aka common elements, by running the following command: `sackL & sackR` which yields us the 
answer `{'a'}` so we know that `'a'` is the only common element amongst the two partitions. 

### Calculating Priorities

Calculating the priority of each common element is relatively easy once we familiarize ourselves with the `ord()` function 
in python, an equivalent probably exists in your language of choice, which simply returns the ASCII value of character.

Lets examine its behaviour:

- `ord('a') == 97`
- `ord('A') == 65`

As we can see the function simply returns the ASCII value but the problem assigns priorities based on their own custom
scale from 1-52. So all we got to do is subtract a certain number from each ASCII value, aka a shift, so that we fall 
into the desired range.

For lowercase characters, the shift value is `96`. Note that `ord('a') - 96 == 1`  as desired.

For uppercase characters, the shift value is `38`. Note that `ord('A') - 38 == 27` as desired.

So for any other uppercase or lowercase characters our shift values ensure that we fall into the correct
domain of priorities. For example, `ord('p') - 96 == 16` as intended and similarly for uppercase characters.

## Answer

The answer for this problem is **8252**.

This answer is true for my given specialized input data. Note that every AOC user will not receive the
same input data for even the same problem.