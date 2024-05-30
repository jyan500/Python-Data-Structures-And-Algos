/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
/*

Approach:
s1 = a a b c c 
s2 = d b b c a

s3 = a a d b b c b c a c

iterate through the longer string, and try to match characters to the shorter string
keep track of 3 pointers, 
one for s1, s2, and s3 (i, j and k respectively)

at each k, we check whether our current value for index at s1 or s2 is equal to s3[k],
if so, we increment down either s1 or s2, and s3 to show that we've successfully matched this character
and are moving onto the next one

base case:
if we've reached the end of s1 and s2, that means we've successfully
matched all characters
recurrence relation:

if (they're both equal)
    increment down s1 but not s2 OR
    increment down s2 but not s2 

    (this is where the backtracking comes in, where if going down s1 doesn't work out,
    you'll need to backtrack to go down the s2 path, which means you may be revisiting
    the same characters multiple times)
    
else if (char at s1 === s3[k])
    increment down s1 
else if (char at s2 === s3[k])
    increment down s2
else (if neither character is equal to s3[k])
    we return false, since we can't match any further

Memoization:
At each k, i and j, we store the result of whether its possible to match the remainder of i
and j with the remainder of k

Time Complexity: O(len(s1) * len(s2))
Space: O(len(s1) * len(s2))

Example:
s1 = abee
s2 = abjf

s3 = ababjeef

i = 0, j = 0, k = 0

s3[k] is "a", and both s1[i] and s2[j] are "a", increment i first

i = 1, j = 0, k = 1
we hit case 1 where s1[i] and s2[j] are matching with s3[k]
here, we can match b with s1 again

i = 2, j = 0, k = 2
here, we cannot match "a" (s3[k]), but 
we can match s3[2] === s2[0], so we increment j and k

i = 2, j = 1, k = 3
we can match s3[3] === s2[1], so we increment j and k

i = 2 , j = 2, k = 4
we can match s3[4] === s2[2], so we can increment j and k

i = 2, j = 3, k = 5 
we can match s3[4] === s1[2], so increment i and k

i = 3, j = 3, k = 6
we can match s3[6] === s1[3], so increment i and k

i = 4, j = 3, k = 7
we can match s3[7] === s2[3], so increment j and k

at this point, i and j have reached the end, so return true

*/
var isInterleave = function(s1, s2, s3) {
    /*
    if the length of the two smaller strings is not equal
    to the length of the main string, then it's not possible
    to interleave by default, since every character in s3 needs 
    to match with a character in s1 and s2
    */
    if (s1.length + s2.length !== s3.length){
        return false  
    }
    let memo = {}
    var search = function(i, j, k) {
        // if able to reach both ends of s1 and s2, this is valid
        if (i >= s1.length && j >= s2.length){
            return true
        }
        if (`${i},${j},${k}` in memo){
            return memo[`${i},${j},${k}`]
        }
        // if either can be chosen, increment down either s1 or s2 (but not both, since that'd mean you match two characters on s3)
        if (s3[k] === s1[i] && s3[k] === s2[j]){
            memo[`${i},${j},${k}`] = search(i+1,j,k+1) || 
            search(i,j+1,k+1)
        }
        // choose a path down s1
        else if (s3[k] === s1[i]) {
            memo[`${i},${j},${k}`] = search(i+1,j,k+1)
        }
        // choose a path down s2
        else if (s3[k] === s2[j]){
            memo[`${i},${j},${k}`] = search(i,j+1,k+1)
        }
        // if neither character is equal to the character at s3,
        // return false
        else {
            memo[`${i},${j},${k}`] = false
        }
        return memo[`${i},${j},${k}`]
    }
    return search(0,0,0)
};