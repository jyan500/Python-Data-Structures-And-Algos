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
    /*
    To encode the string, I would loop through the list of strs,
    and then place a delimiter between each string. The delimiter would be two characters,
    the length of the string, as well as an additional delimiter, to avoid an edge case
    where the string itself contains a number, which would make a single number delimiter invalid.
    Depending on what characters are allowed, I would choose the characters that aren't allowed
    in a string to be a delimiter. The reason why I need the length of the string is because without it,
    if you attempted to decode, you wouldn't know exactly where the end of the string was, just relying on 
    trying to check for the next delimiter wouldn't work for similar reasons, like if you had
    4#ab3c1#a,
    here, you can't rely on the number as the end of the word because "c" is the end of the word and not "3",
    but if you know the length beforehand, you'll know that from a to c is length 4, so that's the right word.
    */
    encode(strs) {
        let res = []
        for (let i = 0; i < strs.length; ++i){
            let delimeter = strs[i].length.toString() + "#"
            res.push(delimeter)
            res.push(strs[i])
        }
        return res.join("")
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    /*
    To decode the string, I would start looping through the string. Whenever 
    I see a number immediately followed by the delimiter, I know that this is the beginning
    of a word. So I will slice from the index of the delimiter + 1 to the end of the word indicated by the 
    number within the delimiter in order to get the string. Then I push it into an array and
    return after looping through the whole string
    In order to account for edge cases where the number is more than one digit, I will perform a while loop
    until the index is no longer a number
    */
    decode(str) {
        let res = []
        let i = 0
        while (i < str.length){
            let curLength = ""
            // continue looping until str[i] is no longer a number,
            // this is to avoid edge cases where the length of an individual string is greater than 9
            while (!isNaN(parseInt(str[i]))){
                curLength += str[i]
                ++i
            }
            let length = parseInt(curLength)
            // check to make sure str[i] is a number, and str[i+1] is "#"
            if (str[i] === "#"){
                res.push(str.slice(i+1, i+1+length))
                // jump to the next delimiter
                i = i + 1 + length
            }
        }
        return res
    }
}


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
