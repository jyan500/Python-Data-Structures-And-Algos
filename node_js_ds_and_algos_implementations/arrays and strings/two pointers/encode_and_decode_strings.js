/*
Approach:
Encode the string like so where the it's the length of the string, followed by a delimter (
in case the string contains integers), and then the string

strs = ["abc", "def", "ghijklmnop"]

encode(strs) would return "3#abc3#def10#ghijklmnop"

decode would iterate through the str,
    iterate until you see a "#", the numbers before this would be the length of the string
    slice the string from i to i + length, and then increment i such that
    you repeat the process of retrieving the length of the string, and then slicing, etc

Time: O(N)
Space: O(1) (no additional memory being used besides the return)
*/
class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = ""
        for (let i = 0; i < strs.length; ++i){
            res += strs[i].length + "#" + strs[i]
        }
        return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = []
        let i = 0
        while (i < str.length){
            let len = ""
            while (str[i] !== "#"){
                len += str[i]
                ++i
            }
            let intLen = parseInt(len)
            ++i
            res.push(str.slice(i, i+intLen))
            i = i + intLen
        }
        return res
    }
}
