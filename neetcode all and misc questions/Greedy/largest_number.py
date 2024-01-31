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
	"""
	Revisited on 1/31/2024,
	Came up with a similar solution O(NLogN) using cmp_to_key, and sorting
	by comparing the numbers a + b, or b + a and seeing which resulted in
	a larger number

	The only difference is that I manually removed leading zeroes to cover
	this edge case: [0, 0],

	whereas neetcode's solution just converts the string into an int, and back
	to a string, which also handles it.
	"""
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key       
        # custom sorting order, sort by
        # whichever number would make a greater number when appending the two together
        # determines the sorting order
        # i.e 30 and 3
        # 303 < 330, so the ordering should be 3 and then 30
        def cmp_items(a, b):
            config1 = str(a) + str(b)
            config2 = str(b) + str(a)
            if int(config1) > int(config2):
                return -1
            elif int(config1) < int(config2):
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(cmp_items))
        # this handles case of empty zeroes, like 
        # [0, 0, 0], if i gets to len(nums)-1, 
        # we slice out from [i: ]
        # you only need to remove up to the last zero
        i = 0
        while (i < len(nums)-1):
            if nums[i] != 0:
                break
            i += 1
        removedZeroes = nums[i:]
        return "".join([str(n) for n in removedZeroes])
        

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools
        def sortKey(x, y):
            a = int(str(x) + str(y))
            b = int(str(y) + str(x))
            return 1 if a > b else -1
        sortedByBiggest = sorted(nums, key=functools.cmp_to_key(sortKey), reverse=True)
        return str(int("".join([str(n) for n in sortedByBiggest])))