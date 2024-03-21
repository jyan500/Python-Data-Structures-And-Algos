/**
 * @param {number[]} nums
 * @return {number[][]}
 */
/* 
Time Complexity: O(N * (2^N))
Optimized Solution from Neetcode
Example Run Through:

res = []

nums = [1,2,2,3]
1st recursive call 
i = 0
cur = []
search(1, [1])

2nd recursive call
i = 1
cur = [1]
search(2, [1, 2])

3rd recursive call
i = 2
cur = [1, 2]
search(3, [1, 2, 2])

4th recursive call
i = 3
cur = [1, 2, 2]
search(4, [1, 2, 2, 3])

5th recursive call
i = 4
cur = [1, 2, 2, 3]
4 >= nums.length, so we add
[1,2,2,3] to res

backtracking to 4th
i = 3
cur = [1, 2, 2]
runs the while loop (it doesn't run since i + 1 >= nums.length)
search(4, [1, 2, 2])

6th recursive call
i = 4
cur = [1, 2, 2]
4 >= nums.length, so we add
[1, 2, 2] to res

backtracking to 4th call
nothing left to do here, returns nothing 

backtracking to 3rd call
i = 2
cur = [1, 2]

runs while loop
nums[2] !== nums[3] (2 !== 3),
so while loop doesn't run
search(3, [1,2])

7th call
i = 3
cur = [1, 2]
search(4, [1, 2, 3])

8th call
i = 4
cur = [1, 2, 3]
4 >= nums.length, so we add 
[1, 2, 3] to res

backtracking to 7th call
i = 3
cur = [1, 2]
while loop, doesn't run because 3 + 1 >= 4
search(4, [1,2])

9th call
i = 4
cur = [1, 2]
4 >= nums.length, so we add
[1, 2] to res

backtracking to 7th call
nothing left to do here, returns nothing

backtracking to 3rd call
nothing left to do here, returns nothing

backtracking to 2nd call
i = 1 
cur = [1]

while loop runs,
nums[1] === nums[2] (2 === 2), so ++i

i = 2
nums[2] !== nums[3], so break at i = 2
search(3, [1])

8th call:
i = 3
cur = [1]
search(4, [1, 3])

9th call:
i = 4
cur = [1, 3]
4 >= nums.length,
appends [1,3] to res

backtracking to 8th call
i = 3
cur = [1]
while loop doesn't run because 3 + 1 >= 4
search(4, [1])

10th call:
i = 4
cur = [1]
4 >= nums.length
appends [1] to res

backtracking to 8th call:
nothing left to do, returns nothing

backtracking to 2nd call:
nothing left to do, returns nothing

backtracking to 1st call:
i = 0
cur = []
runs while loop
nums[0] !== nums[1], so doesn't run

search(1, [])

11th call:
i = 1
cur = []
(now it's just 2 by itself)
search(2, [2])

12th call:
i = 2
cur = [2]
search(3, [2, 2])

13th call:
i = 3
cur = [2, 2]
search(4, [2, 2, 3])

14th call:
i = 4
cur = [2, 2, 3]
4 >= nums.length
res appends [2, 2, 3]

backtracking to 13th call
i = 3
cur = [2, 2]
while loop runs
3 + 1 >= 4 so doesn't run
search(4, [2,2])

15th call:
i = 4
cur = [2, 2]
4 >= nums.length
res appends [2, 2]

backtracking to 13th call,
nothing left to do here, returns nothing

backtracking to 12th call
i = 2
cur = [2]
while loop runs
nums[2] !== nums[3], while loop breaks
search(3, [2])

16th call:
i = 3
cur = [2]
search(4, [2, 3])

17th call:
i = 4
cur = [2, 3]
4 >= nums.length
appends [2, 3] to res

backtracks to 16th call:
i = 3
cur = [2]
while loop
3 + 1 >= 4, while loop doesn't run
search(4, [2])

18th call:
i = 4
cur = [2]
4 >= nums.length
appends [2] to res

backtracks to 16th call:
nothing left to do, returns nothing

backtracks to 12th call:
nothing left to do, returns nothing

backtracks to 11th call
i = 1
cur = []
while loop
nums[1] === nums[2], so we increment i to 2 
(this loop iteration prevented a duplicate from occurring!)
nums[2] !== nums[3], breaks

search(3, [])

17th call:
i = 3
cur = []
search(4, [3])

18th call:
i = 4
cur = [3]
4 >= nums.length, so
[3] is appended to res

backtracks to 17th call
i = 3
cur = []
while loop
3 + 1 >= 4, while loop doesn't run
search(4, [])

19th call:
i = 4
cur = []
4 >= nums.length, so
[] is appended to res

backtracks to 17th call
nothing left to do here, returns nothing

backtracks to 11th call
nothing left to do here, returns nothing

backtracks to 1st call
nothing left to do returns nothing

Final result:
[[1,2,2,3], [1,2,2], [1,2,3], [1,2], [1,3], [1], [2,2,3], [2,3], [2], [3], []]

*/
var subsetsWithDupOptimized = function(nums) {
    nums.sort()
    let res = []
    var search = function(i, cur){
        if (i >= nums.length){
        	res.push(cur)
            return
        }
        search(i+1, [...cur, nums[i]])
        /* the key difference is that in a case of a sorted array with duplicate nums,
        this loop helps us find the next unique subset that we'd need to recur on by not including
        the number at i
        */
        while (i + 1 < nums.length && nums[i] === nums[i+1]){
        	++i
        }
        search(i+1, cur)
    }
    search(0, [])
    return res
};
/*
Time Complexity: O(N *(2^N))
Naive Solution: 
Similar to subsets 1, except we need to sort nums first.
And then we either include nums[i], or we don't

This would get all 2^N calls, a slightly optimized version from neetcode above avoids this
and also avoids a few extra calls trying to convert a set back to an array
*/
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums.sort()
    let res = new Set()
    var search = function(i, cur){
        if (i >= nums.length){
            res.add(cur.join(","))
            return
        }
        search(i+1, [...cur, nums[i]])
        search(i+1, cur)
    }
    search(0, [])
    return [...res].map((x) => x !== "" ? x.split(",") : [])
};