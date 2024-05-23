/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    /*
    we're only interested in the length of the subsequence and not the actual
    subsequence itself. 
    2-D Dynamic Programming Problem
    
    dabce
    acef
    
    recurrence relation
    using two pointers
    keep one pointer the same, and increment the other pointer if the values are not the same
    if the both the values are the same, increment both pointers, and add 1 to the result of the recursive call
    and return
    what is the max common subsequence length that can be achieved with these two pointer positions?
    
    i = 0 j = 0 
    d != a, increment i
    i = 1 j = 0
    a == a, 
    i = 2 j = 1
    b != c, increment i
    i = 3 j = 1
    c == c, increment i and j
    i = 4 j = 2
    e == e, increment i and j
    i has reached the end

    when memoizing, we use i,j as the key, and the value is the max length common subsequence
    that can be created starting from these indices i,j 

    Time Complexity (With memoization):
    O(N1*N2), which is the total amount of distinct subproblems 

    Space:
    O(N1*N2)

    */
    let memo = {}
    N1 = text1.length
    N2 = text2.length
    var search = function(i, j){
        if (i >= N1 || j >= N2){
            return 0
        }
        else if (`${i},${j}` in memo){
            return memo[`${i},${j}`]
        }
        else if (text1[i] === text2[j]){
            let res = 1 + search(i+1, j+1)
            memo[`${i},${j}`] = res
            return memo[`${i},${j}`]
        }
        else {
            let res1 = search(i, j+1)
            let res2 = search(i+1, j)
            memo[`${i},${j}`] = Math.max(res1, res2)
            return memo[`${i},${j}`]
        }
    }
    
    return search(0, 0)
};