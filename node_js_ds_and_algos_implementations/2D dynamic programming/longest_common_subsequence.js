class Solution {
    /**
     * @param {string} text1
     * @param {string} text2
     * @return {number}
     */
    longestCommonSubsequence(text1, text2) {
        /*
        backtracking problem
        text1= cate
        text2= dcbatcsjaltde

        cate as a subsequence does exist in test2
        but if you were to start counting from the first "c"
        in text2, you would find "cat"

        it seems you will need two pointers
        one to go through index of text1
        and the other for index of text2

        However, we can't always assume that the longest subsequence will start at 0

        for example, the longest subsequence here is "s" which is length 1
        psnw
        vozsh

        this is why we need backtracking, since the longest common subsequence could be found
        by starting at the next index for either i or j
        
        if text1[i] === text2[j]
            recursive call advance j and i
        else
            recursive call that only advances j and keeps i the same
            recursive call that only advances i and keeps j the same
        
        As is, this works but is exponential, because at each given character (if they aren't the same),
        there's two separate decision trees that occur, which could branch off into another set of decision trees,
        2^n

        You can memoize so at a given (i,j), we already know the max subsequence that can occur and return that

        Memoized time complexity: O(M*N)
        Space: O(M*N)
        */
        let i = 0
        let j = 0
        let res = 0
        let memo = {}
        const search = (i,j) => {
            const key = `${i},${j}`
            if (i === text1.length){
                return 0
            }
            if (j === text2.length){
                return 0
            }
            if (key in memo){
                return memo[key]
            }
            if (text1[i] === text2[j]){
                memo[key] = 1 + search(i+1,j+1)
                return memo[key]
            }
            // return the max you can get by either 
            // searching on the left or the right in the case
            // that both strings are not equal
            // try incrementing the index text1 only
            const searchText1 = search(i+1, j)
            // try incrementing the index for text2 only
            const searchText2 = search(i, j+2)
            memo[key] = Math.max(searchText1, searchText2)
            return memo[key]
        }

        return search(0,0)
    }

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