# Milestone 2 Coding Challenge

In this coding challenge, you will implement the merge sort algorithm discussed in [Introduction to Algorithms Lecture 3](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-3-insertion-sort-merge-sort/). **It is easy to find python implementations of merge sort online, but I would strongly encourage you to _not_ refer to any of these**. Recursive algorithms often appear obvious once you’ve seen working code, but the real value is in learning to work out their structure. If you get stuck, feel free to talk to any of the apprentice teachers and we will do our best to help.

In addition to the merge sort implementation, you will write unit test functions and benchmark functions to compare run times against a provided insertion sort function for various list sizes. This should give you some practice with lists and dictionaries, as well as help give a sense of the performance considerations for constant factors vs. asymptotic complexity (e.g. O(*n*<sup>2</sup>) or O(*n* log *n*)).

Part 1: Merge Sort
------------------
In `milestone2/merge_sort.py`, there is a `merge_sort` function defined that currently returns an empty list. This should be updated to return a list containing the sorted members of the input list, using a recursive merge sort algorithm.

A reminder on the basic structure of merge sort: split list into halves repeatedly until only 1 item is in each list, then merge pairs of sub-lists into sorted order until entire list is sorted. Example:
```
Step 1:  [3, 2, 4, 1]     # split in half
Step 2:  [3, 2] [4, 1]    # split in half
Step 3:  [3] [2] [4] [1]  # merge [3] with [2], [4] with [1]
Step 4:  [2, 3] [1, 4]    # merge [2, 3] with [1, 4]
Step 5:  [1, 2, 3, 4]     # done
```

Part 2: Testing
---------------
To run test cases:

> ./run-tests.sh

There is currently one failing test, which should pass once your merge sort function is working. You should add 3 or more additional test cases in `milestone2/tests/test_merge_sort.py` that further verify the correct behavior of your sorting function.

Part 3: Benchmarks
------------------
To run benchmarks:

> ./run-benchmarks.sh

This currently throws an error when run. You should fill in the code in `milestone2/benchmarks/benchmarks.py` wherever there is a `// TODO` comment, after which this script will print run times for your merge sort and an implementation of insertion sort, with varying length lists passed to each. You should be able to verify that merge sort becomes considerably faster than insertion sort as the size of the list being sorted grows.

Extra Credit: Optimization
--------------------------
Once you have running benchmarks, you can begin to try out ways of making your sorting function faster. Copy your merge sort function and add the copied function to the `sort_functions` in `milestone2/benchmarks/benchmarks.py`. Now try to improve the copied function, while re-running the benchmarks to compare your changes. There are no restrictions to what you can try here, though you shouldn't be inventing a whole new sorting algorithm (or implementing a totally different one). If your merge sort was implemented correctly with O(*n* log *n*) complexity, any performance optimizations will likely be modest, so don't expect too much!

Linting
-------

To lint your code (test whether it matches pep8 coding style).

Step 1: Install pep8, which was renamed to pycodestyle:
> pip install pycodestyle

Step 2: Run pycodestyle on `milestone2` directory:
> pycodestyle milestone2 --max-line-length=110