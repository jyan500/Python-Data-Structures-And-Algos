/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    /*
    Approach:
    get total sum of nums
    
    IMPORTANT TIME SAVER:
    the target sum that the subsets should sum to 
    is total sum / 2, if this isn't a whole number (i.e total % 2 != 0)
    we cannot logically split the 
    array into subsets that would sum up to this target since
    every number in the array is a whole number and not a decimal
    the goal here is to continually add numbers until the current === total/2, so we know the remaining subset of numbers we haven't chosen is equal to our current sum. 

    the recurrence relation is a knapsack relation where we either
    1) pick the current element at i and include in our total, increment i OR
    2) increment i but ignore the current element
    since our goal is to return a bool, we return 1) OR 2)
    
    Base case:
    if i >= N, we know there's no subset that we could've found, since that means 
    we chose all the elements
    if total - cur === cur, that means the total sum we've found is equal to the total
    sum of the subset we haven't chosen, so this is a valid answer.
    
    Memoization:
    At each index i and current total, we can store whether we could make a valid subset by including this index. This is different from other 1-D dynamic programming problems encountered
    as it involves a composite key of BOTH the current index and the current running total. The reasoning is that at each i, it's possible we could have a different cur value, so it wouldn't be right to overwrite the recursive return value at one possible i with another.

    Time complexity: O(N*sum), where N is len(nums) and sum is the sum(nums)
    Space complexity: O(N*sum) for the memoization dict
    
    for example:
    nums = [1, 5, 11, 5]
    total = 22
    starting at i = 0,
    we can choose 1 and include it in our cur total, and move to 5, 
    or we can skip 1 and move to 5
    using this recurrence relation, we see that as soon as we choose 1,5,11, for a total of 17
    we see this already greater than total/2, which is 11, so we can return false here and we don't need to continue.
    backtrack to 1, 5, and then instead of picking 11, it'll skip 11 and pick 5
    this time we get 1, 5, 5, which triggers the base case (1+5+5 = 11, total = 22, 22/2 = 11,
    which is total sum of the remaining subset that we haven't chosen, which in this case is just 11 by itself)
    */
    let N = nums.length
    let total = nums.reduce((num, acc) => acc + num, 0)
    if (total % 2 !== 0){
        return false
    }
    let memo = {}
    var search = function(i, cur){
        if (i >= N){
            return false
        }
        if (`${i},${cur}` in memo){
            return memo[`${i},${cur}`]
        }
        if (cur >= total/2){
            return cur === total/2
        }
        memo[`${i},${cur}`] = search(i+1, cur + nums[i]) || search(i+1, cur)
        return memo[`${i},${cur}`]
    }
    return search(0, 0)
};