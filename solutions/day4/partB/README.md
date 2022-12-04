# Day 4 Part B - Solution

It is tradition for AOC problem sets to have an easier second part if you have done the first part of the problem set
correctly. This case is no different as part B of the problem set is actually an easier problem to tackle once
you have figured out the parsing and string manipulation problems that need to be tackled in part A. The main trick to 
tackle this problem is explained below!

Simply run the script and view the terminal's output to view the answer. However, make sure that 
`FILE_MODE_REAL_INPUT_MODE` is set to true if you want to run the script against the problem input data the AOC challenge 
expects you to solve. Setting it to false will run the script against the contents of `test.txt` which is a 
test case presented in the problem itself. 

## Problem Difficulty (1-10)

1/10

## Solution Explanation

### Parsing Input Data (Same as Part A)

So this time around the AOC challenge stepped their game up when it comes to the format of these input files. The format
of the file this time around was much more complicated to parse but nonetheless if you are familiar with string 
manipulation it shouldn't have been a game changer.

Let's examine the structure of the file to determine our parsing method. 

The file contains lines in the following form: `A-B,X-Y` where `A,B,C,D` are all integers. What we need to do is 
find a way to extract these values from the presented string. 

So first thing first is that the comma denotes the separation of pairs, so we can extract each range in the following
manner: `'A-B,X-Y'.split(',') == ['A-B', 'X-Y']` which is exactly what occurs on **line 10** of the solutions.

Then we need to extract the integer values from the ranges with the form `A-B` which can be simply done again using 
`split()` but this time using the dash as the seperator. So `'A-B'.split('-') == ['A', 'B']`. Which is what happens on
**line 13** of the solutions but note that I store the pairs now in the following form `(['A','B'], ['X', 'Y'])` which 
is just a tuple of arrays.

We have basically tackled the main monster here and all that is left is looping over these tuples and converting each 
element in the array to an integer by using `int()` before we can analyze these ranges.

### Finding Intersections

There is a very simple way to do this if you don't care about code efficiency. In light of the competitive nature of AOC, 
this is the approach I will be presenting. 

The intuition is that a range like `5-8` can be easily represented as a set in the following form `{5,6,7,8}` since 
this is a discrete range, a range in which all the step values have to be integers, i.e 5.3 is not in the range.

If we are able to convert the given range `X-Y` to a set including all the numbers described in the range
then we can simply run the python built-in intersection command against two sets `X & Y` and then check the length
of its intersection. As long as there exists an element in `X & Y` we know that there is an overlapping element amongst
the sets and hence the ranges overlap. 

So how do we convert a range like `5-10` to a set?

Simply use the `range()` function and then convert the result into a set. So we would run `range(5, 10 + 1)`, we add
1 to 10 because `range()` excludes the endpoint. Then we can convert the result into a set `set(range(5,11))`.

So assume we do that twice for both ranges, and we thus have the two following sets `x, y`.

To check if there is a common element, i.e overlapping element, we simply check the length of the intersection. 

This can be done simply by `len(x & y)`, if this is positive we know there is an overlapping element, and then we simply 
add one to the running total which is what is done on **line 30** of the solution set. 

**NOTE:** There is a better solution to do this for sure, however I went with the approach that would take the least 
amount of time to code. So please don't feel like that this approach is optimal. This is the natural approach that
occurred to me whilst programming in attempts to make the leaderboard. Sadly, OpenAI solutions are keep beating me :(

## Answer

The answer for this problem is *794*.

This answer is true for my given specialized input data. Note that every AOC user will not receive the
same input data for even the same problem.