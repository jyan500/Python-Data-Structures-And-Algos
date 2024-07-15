/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
/* 
https://leetcode.com/problems/assign-cookies/
Approach:
1) Sort the greed factors and the sizes of the cookies in ascending order, 
    this is a greedy approach, we're always finding the smallest possible cookie that can be assigned to meet the
    greed factor.

2) Keep track of the count to show that this cookie was assigned to a greed factor
3) Use two pointers, i and j to iterate through the greed factors and the cookies at the same time.
    if the size of the cookie >= greed factor
        increment both i and j, as well as the count to show that this cookie was assigned to a greed factor
    else
        only increment j (size of the cookie) to see if a bigger cookie can satisfy the greed factor
4) return count
*/
var findContentChildren = function(g, s) {
    var sortKey = function(a, b){
        if (a < b){
            return -1
        }
        else if (a > b){
            return 1
        }
        return 0
    }
    g.sort(sortKey)
    s.sort(sortKey)
    let i = 0
    let j = 0
    let count = 0

    while (i < g.length && j < s.length){
        if (s[j] >= g[i]){
            ++i
            ++j
            ++count
        }
        else {
            ++j
        }
    }
    return count
};