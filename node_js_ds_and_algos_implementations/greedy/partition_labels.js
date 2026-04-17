/**
 * @param {string} s
 * @return {number[]}
 */
class Solution {
    /**
     * @param {string} S
     * @return {number[]}
     */
    partitionLabels(S) {
        /*
        Revisited 4/17/2026
        O(N) Time
        O(26) Space
        1) figure out the first and last occurrence of each character and store in map,
        to figure out the last occurrence, we just keep overwriting the 2nd value in an array
        until it doesn't get updated anymore.

        2) as we iterate, we check the first and last occurrence of the current string at index i
        and we also keep track of our current window indices, curStart and curEnd
        if the first occurrence > curEnd,
            that means a new substring has started,
            so we record the current length (curEnd - curStart + 1),
            then restart the current window starting at i
        */
        const map = {}
        for (let i = 0; i < S.length; ++i){
            // keep overwriting the 2nd spot,
            // the very last overwrite will be the last time
            // that character is seen in the array
            if (!(S[i] in map)){
                map[S[i]] = [i, i]
            }
            else {
                map[S[i]][1] = i
            }
        }
        // as we iterate through, we know that based on the substrings we find,
        // for example, x, we know x will need to be at the length until the
        // last occurrence of x is found,
        // since we can't have repeated characters across substrings
        let curStart = 0
        let curEnd = 0
        let output = []
        for (let i = 0; i < S.length; ++i){
            let [first, last] = map[S[i]]
            // if the character we're at is already out of the bounds of the last
            // character boundary, this is the start of a new substring
            // this also covers cases where the character only appears once in the substring,
            // which would allow us to create a substring of length 1
            // for example xyxxyzbzbbisl
            // once we get to the first i, curStart = 10, curEnd = 10
            // but then we get to s, we see the first, last is both 11, which is greater than curEnd,
            // so we record the length of the previous substring, which was 1
            if (first > curEnd){
                output.push(curEnd-curStart+1)
                curStart = i
                curEnd = i
            }
            curEnd = Math.max(curEnd, last)
        }

        // note the last element won't reach the conditional to break
        // into a new substring, have to check manually
        output.push(curEnd-curStart+1)
        return output

    }
}

var partitionLabels = function(s) {
    /*
    https://www.youtube.com/watch?v=B7m8UmZE-vw
    the letters in one partition cannot appear in another partition
    make as many partitions as possible meeting this condition
    1) hashmap to get the index of the last occurrence of each character in S,
    we simply just set last[s[i]] = i, so that the value keeps overwriting itself until the last occurrence is seen,
    and that would be the end value of that key
    
    2) Two pointers, keep a size and "end" variable to denote the end of the current partition
    
    The idea is that when iterating through S, based on the first letter we see, we want to see what the last occurrence
    of this letter is. Then, set the end of the partition to the last occurrence of this letter so that we don't repeat the same letter
    later on.
    As we iterate, we check to see if any letter between the end of the partition and our current index has a last occurrence
    that is AFTER our end of partition. In that case, we'd need to update the end of partition
        
    However, if our current index === end of partition, this means that any character before the end of partition occurs only within
    this partition, so we can count this as "one" partition and record the size, and reset the size to 0.

    O(N) time
    O(26) space
    */
    let last = {}
    for (let i = 0; i < s.length; ++i){
        last[s[i]] = i
    }
    let size = 0
    let res = []
    let end = 0
    for (let i = 0; i < s.length; ++i){
        if (last[s[i]] > end){
            end = last[s[i]]
        } 
        ++size
        if (i === end){
            res.push(size)
            size = 0
        }

    }
    return res
};