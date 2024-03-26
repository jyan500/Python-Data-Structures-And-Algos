/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    /*
    because we want unique combinations, we should sort first
    candidates = [2,5,2,1,2]
    after sorting
    candidates = [1,2,2,2,5]
    1,2,2
    
    In a very similar fashion to the subsets II problem, our recurrence relation is that
    1) Include the current element into our current list, and increment i, subtract the current element off of target. Because we can't include the same element at the index more than once, we have to increment i each time.
    2) Don't include the current element into our current list, and increment i, but also leave target the same since we didn't choose the element at i
    
    The base is that if our target <= 0 OR i exceed the length of our candidates list:
        if target is exactly 0, we've found a combination, so append. Otherwise we just return nothing
    
    In order to prevent duplicates, we apply a similar logic from subsets II:
    we need to do a while loop that increments i each time candidates[i] === candidates[i+1] as long as i + 1 < candidates.length
    this is to avoid paths in the recursion that result in the same combinations being chosen as a result of having the same 
    starting number. 
    
    Example Execution:
    [1, 2, 2, 2, 5]
    target = 5
    
    1st recursive call
    i = 0
    cur = []
    target = 5
    search(1, 4, [1])
    
    2nd recursive call
    i = 1
    cur = [1]
    target = 4
    search(2, 2, [1, 2])
    
    3rd recursive call
    i = 2
    cur = [1, 2]
    target = 2
    search(3, 0, [1, 2, 2])
    
    4th recursive call
    i = 3
    cur = [1, 2, 2]
    target === 0
    so append [1, 2, 2] to cur
    
    backtracking to 3rd call
    i = 2
    cur = [1, 2]
    target = 2
    enters while loop, i + 1 < 5 and candidates[2] === candidates[3]
    increments i to 3
    3 + 1 < 5, candidates[3] !== candidates[4], breaks
    by doing this, we've avoided a duplicate case where we would've appended [1, 2, 2] to our list again,
    since we skipped the "2" element at candidates[3]
    search(4, 2, [1, 2])
    
    5th recursive call
    i = 4
    cur = [1, 2]
    target = 2
    search(5, 2 - 5 = -3, [1, 2, 5])
    
    6th recursive call
    i = 5
    cur = [1, 2, 5]
    target = -3
    this is not a valid combination
    
    backtracking to 5th call
    nothing left to do here, return nothing
    
    backtracking to 3rd call
    nothing left to do here
    
    backtracking to 2nd call
    i = 1
    cur = [1]
    target = 4
    enters while loop, 1 + 1 < 5, candidates[1] === candidates[2] 
    increments i, i = 2
    2 + 1 < 5, candidates[2] === candidates[3]
    increments i, i = 3
    3 + 1 < 5, candidates[3] !== candidates[4], breaks
    search(4, 4, [1])
    
    7th call
    i = 4
    target = 4
    cur = [1]
    search(5, 4 - 5 = -1, [1, 5])
    
    8th call
    i = 5
    target = -1
    cur = [1, 5]
    this is not a valid combination
    
    backtracking to 7th call
    i = 4
    target = 4
    cur = [1]
    while loop, 5 is not less than 5, so we can't enter the while loop
    search(5, 4, [1])
    
    9th call
    i = 5
    target = 4
    cur = [1]
    this is not a valid combination, and also cannot go any further since i is the same
    as the length of combination
    
    backtracking to 7th call
    nothing to do here, return nothing
    
    backtracking to 2nd call,
    nothing to do here, return nothing
    
    backtracking to 1st call
    i = 0
    cur = []
    target = 5
    while loop entered, candidates[0] !== candidates[1]
    search(1, 5, [])
    
    10th call
    i = 1
    cur = []
    target = 5
    search(2, 3, [2])
    
    11th call
    i = 2
    cur = [2]
    target = 3
    search(3, 1, [2, 2])
    
    12th call
    i = 3
    cur = [2, 2]
    target = 1
    search(4, -1, [2, 2, 2])
    
    13th call
    i = 4
    cur = [2, 2, 2]
    target = -1
    this is not valid combination 
    
    backtracking to 12th call
    i = 3
    cur = [2, 2]
    target = 1
    while loop entered, 3 + 1 < 5, candidates[3] !== candidates[4]
    search(4, 1, [2, 2])
    
    14th call
    i = 4
    cur = [2, 2]
    target = 1
    search(5, -4, [2, 2, 5])
    
    15th call
    not valid
    
    backtracking to 14th
    nothing left to do, return nothign
    
    backtracking to 12th
    nothing left to do
    
    backtracking to 11th call
    i = 2
    cur = [2]
    target = 3
    while loop, 2 + 1 < 5, candidates[2] === candidates[3] true,
    increments i, i = 3
    3 + 1 < 5, candidates[3] !== candidates[4] false
    search(4, 3, [2])
    
    15th call
    i = 4
    cur = [2]
    target = 3
    search(5, 3 - 5 = -2, [2, 5])
    
    16th call
    i = 5
    cur = [2, 5]
    target = -2
    not valid
    
    backtracking to 15th,
    nothing to do here
    
    backtracking to 11th call
    nothing to do here
    
    backtracking to 10th call
    i = 1
    cur = []
    target = 5
    
    while loop entered
    1 + 1 < 5, candididates[1] === candidates[2]
    i increments, i = 2
    2 + 1 < 5, candidates[2] === candidates[3]
    i increments, i = 3
    3 + 1 < 5, candidates[3] !== candidates[4], loop breaks
    search(4, 5, [])
    
    17th call
    i = 4
    cur = []
    target = 5
    search(5, 0, [5])
    
    18th call
    i = 5
    cur = [5]
    target = 0
    this is valid since target === 0, append [5] to res
    
    backtracking to 17th
    nothing to do here
    
    backtracking to 10th call 
    nothing to do here
    
    backtracking to 1st call
    nothing left to do, returns
    
    final result =
    [[1,2,2], [5]]
    */

    candidates.sort()
    let res = []
    var search = function(i, target, cur){
        if (target <= 0 || i >= candidates.length){
            if (target === 0){
                res.push(cur)
            }
            return
        }
        search(i+1, target - candidates[i], [...cur, candidates[i]])
        while (i + 1 < candidates.length && candidates[i] === candidates[i+1]){
            ++i
        }
        search(i+1, target, cur)
    }
    search(0, target, [])
    return res
};