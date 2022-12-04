# 2022 - Advent of Code 

![img](assets/aoc_banner_resized.jpeg)

![img](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![img](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F{payamyek}1212%2Fhit-counter)

This holiday season I have decided for the first time to partake in the 2022 [Advent of Code](https://adventofcode.com/) 
(AOC) challenge. The AOC challenge presents two sets of problems every day leading up to Christmas day. In light of the 
Christmas spirit, I will be documenting all my solutions and providing detailed and precise annotations to allow potential 
readers to improve in future AOC challenges.


# Progress

| Day                                      | Part 1       | Part 2      |
|------------------------------------------|--------------|-------------|
| [1](https://adventofcode.com/2022/day/1) | ⭐ | ⭐ |
| [2](https://adventofcode.com/2022/day/2) | ⭐ | ⭐|
| [3](https://adventofcode.com/2022/day/3) | ⭐ | ⭐|
| [4](https://adventofcode.com/2022/day/4) | ⭐ | ⭐|

# Format of Solutions

The solutions posted will be more polished than their initial state used to complete the AOC challenges and can be found under the `solutions/*` directory.

This repository will be structured in the following way, for every day of the challenges there will be a folder named 
`dayi`, where `i` is an integer detailing the day of the challenge. With two sub folders `dayi/partA` and `dayi/partB` 
each containing four files: `input.txt`, `test.txt`,`solution.py` and `README.MD`.

- `input.txt` is the text file containing the input file of the problem set
- `test.txt` is the text file containing a test case of the problem set
- `solution.py` is the python file containing the solution
- `README.md` provides further insight into how the solution works and the nature of the solution and problem

# Focus of Solutions

As programmers, we are occasionally told to write optimized code and code that is highly efficient on a consistent basis. However, this is not the place for it in my opinion. The AOC challenges measure a programmer's proficiency in writing code extremely fast and code optimization simply serves no purpose in these challenges as the provided `input.txt` files are small in size. Hence, even if we were to optimize the codebase these optimizations will not be realized in these challenges. 

So my posted solutions are a result of two main points of focus:
1. Writing code that is readable
2. Writing code quickly without regard for optimizations 

We want to write readable code because typically the second part of the problem set will require you to build upon your pre-existing codebase. 

Secondly, to make the leaderboard we can't spend time optimizing code as that will result in no noticeable benefits and will just increase your submission time. 

# Caveat

Note that each problem has a input file that is feed into the script but this input data is not the same for all users
and thus make sure to use your own input file to run against the script to get accurate results for your tailored problem.
i.e the `input.txt` might differ from person to person, so make sure to use your own data set to calculate the answer
properly for your inputs.
