class Solution {
    /**
     * @param {string} word1
     * @param {string} word2
     * @return {string}
     */
    mergeAlternately(word1, word2) {
        /* two pointers, 
        get char from word1 then word2, iterate both pointers. Then check to see if one of the pointers hasn't reached the end,
        and append the remaining chars
        O(N) Time
        O(1) Space
        */
        let res = [] 
        let i = 0
        let j = 0
        while (i < word1.length && j < word2.length){
            res.push(word1[i])
            res.push(word2[j])
            ++i
            ++j
        }
        if (i < word1.length){
            for (let k = i; k < word1.length; ++k){
                res.push(word1[k])
            }
        }
        else if (j < word2.length){
            for (let k = j; k < word2.length; ++k){
                res.push(word2[k])
            }
        }
        return res.join("")
    }
}
