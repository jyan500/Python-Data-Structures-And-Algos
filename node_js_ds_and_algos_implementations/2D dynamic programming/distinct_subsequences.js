/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
/*
https://leetcode.com/problems/distinct-subsequences/submissions/
Approach:

1) S is always the longer string, and T is the shorter string
since T needs to be found in S. Check this before getting into the recursion.

2) Recurrence relation is a knapsack relation,
using 2 pointers:
    if char in T matches char in S
        I can include S[i] in subsequence,
        and then increment j to match the next char of T OR
        skip to the next char in S and keep the char at T the same
    if char in T doesn't match char in S
        increment i to check the next char of S, but keep the char of T the same

Base Case:
if one of the pointers reaches the end of T, that means I found a valid subsequence, return 1
if one of the pointers reaches the end of S, that means that I didn't find a valid subsequence, return 0

Note that you check the pointer reaching the end of T (the shorter string) first, since there might be cases
where the pointers reach BOTH end of T and end of S, which should still return 1 in that case since a valid subsequence
is found.

Time Complexity:
With memoization, O(M*N), where M is the length of S, and N is the length of T,
since for each value in M you still need to go through all values of T to check if T is found in M,
but the memoization avoids any redundant cases where you already know how many possible subsequences
can be found at a given char in S.

Space:
O(M*N), since you need to store each i,j for S and T

*/
var numDistinct = function(s, t) {
    let M = s.length
    let N = t.length
    // problem assumes that the length of T must be
    // less than the length of S, so s.length must be greater than T, otherwise we can't continue
    if (M < N){
        return 0
    }
    /*
    Storing the i, j as key and the amount of subsequences that can be created starting at this i, j
    */
    let memo = {}
    var search = function(i, j){
        /* If we reached end of T, we've found a subsequence, return 1*/
        if (j >= N){
            return 1
        }
        /* 
        if we reach the end of S without having
        reached end of T, this means we didn't
        find a subsequence, return 0
        */
        if (i >= M){
            return 0
        }
        if (`${i},${j}` in memo){
            return memo[`${i},${j}`]
        }
        if (s[i] === t[j]){
            // knapsack relation, if we found a matching char
            // include s[i] in the subsequence, or skip it
            memo[`${i},${j}`] = search(i+1, j+1) + search(i+1, j)
            return memo[`${i},${j}`]
        }
        else {
            // if no matching char, keep searching down S
            memo[`${i},${j}`] = search(i+1, j)
            return memo[`${i},${j}`]
        }
        
    }
    return search(0, 0)
};