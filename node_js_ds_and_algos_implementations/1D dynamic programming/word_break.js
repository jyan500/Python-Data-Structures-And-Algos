class Solution {
    /**
     * @param {string} s
     * @param {string[]} wordDict
     * @return {boolean}
     */
    wordBreak(s, wordDict) {
        /* 
        determine whether we break at i and start a new string,
        or continue adding to the same string

        rather than storing the actual subString we've created,
        we can just store the beginning of it,
        so we can just calculate slice(beginningIndex, currentIndex) to see
        if the substring is in the word dict

        For memoization, 
        note that you only need to memoize the "beginningIndex", since what we're determining is
        whether at this starting Index, can you split the rest of the words? You don't need to include i
        since we only make a decision if a word is actually created from beginningIndex to i, and not at every i
        */
        let words = new Set(wordDict)
        let N = s.length
        let memo = {}
        const search = (i, beginningIndex) => {
            const cur = s.slice(beginningIndex, i+1)
            if (i === N){
                // if we make it to the end, and our current is also in the word dict,
                // that means we broke up the words successfully
                return words.has(cur)
            }
            let key = `${beginningIndex}`
            if (key in memo){
                return memo[key]
            }
            if (words.has(cur)){
                // we can include this and cur starts over at the current character as the beginingIndex, or continue
                memo[key] = search(i+1, i+1) || search(i+1, beginningIndex)
                return memo[key]
            }
            memo[key] = search(i+1, beginningIndex)
            return memo[key]
        }
        return search(0, 0)
    }
}

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
/*
Approach:
1) Track a starting and ending index for a substring within string S
2) Starting at start = 0, end = 0, we keep incrementing end until we 
find a substring that's in the word dictionary. If so, we then set the start and end to be the same
(end + 1). If not, we continue incrementing the end variable
3) If the end >= length of the original string S, this is the base case. We check to see
if the current substring matches a word in the word dict. This indicates that we should've been able to
split the word fully, so return true if so.
4) If not, we need to backtrack to the case where we found a word, and then go down a separate branch of recursion
by incrementing end + 1 to try and find another valid substring that matches in the word dict. This is the reason
why we have a res variable that stores the result of the case starting from where a valid substring is found,
and then doing res || search(start, end+1) to indicate that only one of these paths needs to be true for the function
to return true.

For example:
word dict = ["hippo", "hip"]
word is "hippo"

We can see in the recursion, we'd hit "hip" first, and then
start the next substring at index 4 ("p")
However, we find that once we reach the end, we would've created the substring
from index 4 to index 5 ("po"), which is not found in the word dict

Therefore, we need to backtrack to where we found "hip" (end index = 3),
and start incrementing. At this point, we would then find "hippo", which is valid and
would return true.

5) The way we apply memoization here is to save the boolean value that tells us whether
we could fully split the substring starting from "start". Therefore, we use the "start" 
index in the memo dict as the key, and the boolean as the value.

With memoization:
Time Complexity: O(N*K), where K is the length of the substring that we're slicing 
Space Complexity: O(N)

*/
var wordBreak = function(s, wordDict) {
    let N = s.length
    let memo = {}
    var search = function(start, end){
        // based on this starting index, can we split the words evenly? If we've already determined
        // this at this starting index, we can reuse the value
        if (start in memo){
            return memo[start]
        }
        if (end >= N) {
            return wordDict.includes(s.slice(start,end+1))
        }
        let res = false
        if (wordDict.includes(s.slice(start,end+1))){
            res = search(end+1, end+1)
        }
        memo[start] = res || search(start, end+1)
        return memo[start]
    }
    return search(0, 0)
};