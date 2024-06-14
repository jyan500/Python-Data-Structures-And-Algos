/**
 * @param {string} s
 * @return {number[]}
 */
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