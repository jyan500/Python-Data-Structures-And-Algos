"""
https://www.youtube.com/watch?v=WDx6Y4i4xJ8&ab_channel=NeetCode

O(NLogN) Time, No additional space

1) The important thing to realize is that we can sort the array based on the fact that when we
compare two numbers, the number that comes first is the one that results in the "bigger" number.

This creates a subproblem where after sorting two numbers, we then take a look at the next set of numbers
to figure out which one would create a bigger number, and then sort that. 

Eventually, the number that creates the biggest number would end up as the last element in the list
(or the first if you do reverse = True on the sort)

2) cmp_to_key from the functools library allows us to write a custom comparator similar to javascript where
you have two params and define the comparison between them, return 1, -1, or 0 in the case the two params are equal

Example:

[3, 30, 34, 5, 9]

Even though the python library doesn't use bubble sort, this will use bubble sort to demonstrate the concept

1st pass 

330 > 303

3 comes before 30

3430 > 3034, so 34 comes before 30

3 34 30 5 9 

530 > 305, so 5 comes before 30

3 34 5 30 9

930 > 309, so 9 comes before 30

3 34 5 9 30

2nd pass

343 > 334, so 34 comes before 3

following comparisons are made ...

34 3 5 9 30

34 5 3 9 30

34 5 9 3 30

3rd pass

534 > 345

following comparisons are made ...

5 34 9 3 30

5 9 34 3 30

4th pass

9 > 5,

9 5 34 3 30

final solution is 

9534330


"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools
        def sortKey(x, y):
            a = int(str(x) + str(y))
            b = int(str(y) + str(x))
            return 1 if a > b else -1
        sortedByBiggest = sorted(nums, key=functools.cmp_to_key(sortKey), reverse=True)
        return str(int("".join([str(n) for n in sortedByBiggest])))