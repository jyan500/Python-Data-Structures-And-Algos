/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
/*
https://leetcode.com/problems/edit-distance/discuss/5241237/java-or-dp-or-top-down
recurrence relation:

when comparing word1 and word2, we think about
the relation between the indices i, j, and what the operation
allows us to increment in order to go further into the recursion

insert:
"horse"
"ros"

if we were to insert "r" to get "rhorse" and "ros", this would
mean that we've successfully matched "r" with this hypothetical character that we just added.
However, because we just added a char, we have to keep i the same, since this "increased" the 
length of the string, so we still need to evaluate the char at word1[i] (in this case "h")
f(i, j+1)

replace:
"horse"
"ros"

if we were to replace "h" with "r", we'd increment both i and j,
since we've successfully matched both characters
f(i+1, j+1)

delete:
"horse"
"ros"

if we were to delete "h", we'd get "orse" and "ros"
in this example, we didn't match any character, but because we haven't matched
a letter in word2 yet, we increment i but keep j the same

f(i+1, j)

Since the question asks for minimum number of operations, we want to take the min of all three operations
and return this. We'd also add one to this result to show that an operation was made at this recursive call
to add onto the min number of operations that we'll be returning in each call.

Edge Case:
if at any point, word1[i] === word2[j],
this means that we can also increment both i and j

Base Case:
if we reach the end of a word, we need to figure out how many remaining operations would be needed to 
get word1 to word2

if end of word1 is reached,
    the number of necessary operations would be the difference in length between word2 and j 
if end of word2 is reached,
    the number of necessary operations would be the difference in length between word1 and i 

Memoization:
at each (i, j), we store the min amount of operations that it'd take to reach word2, given the remaining characters
starting from i, j

Time Complexity (with memoization):
O(M*N), where M is the length of word1 and N is the length of word2
The reasoning is because even with memoization, for each letter of word1, the recursion still takes us through 
through each letter of word2 (Although some of these calls will be O(1) due to retrieving a previously calculated result
from the memoization dict)
Space:
O(M*N)
*/
var minDistance = function(word1, word2) {
    let M = word1.length
    let N = word2.length
    let memo = {}
    var search = function(i, j){
        if (j === N){
            return M-i
        }
        if (i === M){
            return N-j
        }
        if (`${i},${j}` in memo){
            return memo[`${i},${j}`]
        }
        if (word1[i] === word2[j]){
            memo[`${i},${j}`] = search(i+1,j+1)
            return memo[`${i},${j}`]
        }
        let insert = 1 + search(i, j+1)
        let replace = 1 + search(i+1, j+1)
        let del = 1 + search(i+1, j)
        memo[`${i},${j}`] = Math.min(insert, replace, del)
        return memo[`${i},${j}`]
    }
    return search(0, 0)
}; 