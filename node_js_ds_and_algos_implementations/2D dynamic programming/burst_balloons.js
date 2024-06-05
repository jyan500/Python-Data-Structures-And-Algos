/**
 * @param {number[]} nums
 * @return {number}
 */
/*
Will need to revisit this problem in the future, as the explanation isn't 100% clear to me yet.
https://www.youtube.com/watch?v=Hps6bHDGtqQ&ab_channel=NareshGupta
https://www.youtube.com/watch?v=Yz4LlDSlkns&ab_channel=takeUforward
*/
var maxCoins = function(nums) {
    /*
    at each i, when choosing it, you get the value of nums[i-1] * nums[i] * nums[i+1],
    and then i can no longer be chosen
    
    brute force (exponential time O(N^N))
    */
    // var search = function(balloons){
    //     if (balloons.length === 0){
    //         return 0
    //     }
    //     let val = 0
    //     for (let i = 0; i < balloons.length; ++i){
    //         let left = i - 1 < 0 ? 1 : balloons[i-1]
    //         let center = balloons[i]
    //         let right = i + 1 >= balloons.length ? 1 : balloons[i+1]
    //         let total = (left * center * right)
    //         val = Math.max(val, total + search([...balloons.slice(0, i), ...balloons.slice(i+1, balloons.length)]))
    //     }
    //     return val
    // }
    // return search(nums)
    /*
    optimization:
    https://www.youtube.com/watch?v=Hps6bHDGtqQ&ab_channel=NareshGupta
    https://www.youtube.com/watch?v=Yz4LlDSlkns&ab_channel=takeUforward
    1) to avoid index math, you can create a new array with 1's prepended and appended to it
    i.e [3, 1, 5, 8] becomes [1,3,1,5,8,1]
    the boundaries that we want to iterate is from the number 3 to 8, which will
    be our L and R boundaries
    2) important realization is figuring out that this is a 2-D dynamic programming problem, where you create two subproblems
    based on L and R. It also uses reverse thinking:
    the idea is that you want to think of picking balloon i as if it were the "last" balloon to pop, starting from bottom up
    
    For example:
    
    1 3 1 5 8 1
    
    if you were to pick 3, (i = 1), this would mean that you'd get 1 * 3 * 1 as the total
    going one recursion call further, you'll see that there's 2 subproblems, both having a subarray of length 2, that includes the number 3.
    this makes sense since in order for you to pick 3, it had to exist in the subproblem before it.
    
    
    i = 0, l = 1
    i = 1 r = 5
    
    subproblems:
    search(0, 1)                
    search(1,5)
    
    for search(0, 1),
    l is now 0 and r = 1
    because l + 1 === r, we return 0 here since there's nothing to pop
    
    for search(1, 5)
    l is now 1 and r = 5
    the loop starts at l + 1 and goes to r
    the total is calculated as balloons[l] * balloons[i] * balloons[r], which is 
    balloons[1] * balloons[2] * balloons[5], which is 3
    i = 2 ... 5
    search(1, 2)
    search(2, 5)
    
    for search (1,2)
    l is now 1 and r is now 2
    l + 1 === r, we return 0 here
    
    for search(2, 5)
    l is now 2 and r is now 5
    the loop starts at l + 1 and goes to r
    i = 3 ... 5
    the total is calculated as balloons[l] * balloons[i] * balloons[r],
    which is balloons[2] * balloons[3] * balloons[5], which is 5
    search(2, 3)
    search(3, 5)
                            
    for search(2,3),
    l is now 2 and r = 3
    the loop starts at l+1 and goes to r
    l + 1 === r, so we return 0 here
    
    search(3,5)
    l is now 3 and r = 5
    loop starts at l + 1 and goes to r
    i = 4 ... 5
    the total is calculated as balloons[l] * balloons[i] * balloons[r],
    balloons[3] * balloons[4] * balloons[5] = 40
    
    search(3, 4)
    search(4, 5)
    
    you can now see that both of these subproblems will return 0
    
    Now going backwards, you will see subproblems being repeated.
    For example,
    when l = 1 and r = 5
    loop goes from i = 2 ... 5
    the first pass, we did search(1, 2) and search(2, 5)
    however, in the second pass where i = 3 ... 5
    we do search(1, 3) and search(3, 5)
    
    we've actually calculated search(3, 5) already (40), so this is where memoization comes in.
           
    3) You'd memoize (L, R), which tells you the max amount of coins you can get based on the balloons remaining. If you draw out the recursion
    tree like in the video linked above, you will see the repeated subproblems that can be cached
    
    For some reason, using a dict will get a TLE, so you have to use a 2-D array to do the caching

    */
    let N = nums.length+2
    let balloons = [1,...nums,1]
    let memo = initMemo(balloons)
    var search = function(l, r){
        let max = 0
        if (memo[l][r] != -1){
            return memo[l][r]
        }
        for (let i = l+1; i < r; ++i){
            let score = balloons[l]*balloons[i]*balloons[r]
            max = Math.max(max, score + search(l, i) + search(i, r))
        }
        memo[l][r] = max
        return max
    }
    return search(0, N-1)
};

// init memo taken from Neetcode's JS solution
// return a 2-D array with the same amount of rows and columns based
// on the length of nums, each cell filled with -1 initially
var initMemo = (nums) => {
    return new Array(nums.length).fill()
        .map(() => new Array(nums.length).fill(-1));          
}