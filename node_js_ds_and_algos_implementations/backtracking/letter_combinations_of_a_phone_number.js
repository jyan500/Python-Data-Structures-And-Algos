/**
 * @param {string} digits
 * @return {string[]}
 */
/*
Time Complexity: 
if we had an N digit phone number, there are up to 26 different letters for each spot
so O(26^N), but because the max amount of digits is 4, it'd be O(26^4)

Space:
O(1), since there's a constant amount of possibilities listed in the hashmap

*/
var letterCombinations = function(digits) {
    const combinations = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    let res = []
    if (digits === ""){
        return []
    }
    var search = function(i, cur){
    	// base case:
    	// once we've reached i >= digits.length, that means we ran out of digits, so
    	// we push our current letter combination string to res
        if (i >= digits.length){
            res.push(cur)
            return 
        }
        let letterCombinations = combinations[digits[i]]
        // for each digit, iterate through the different letter possibilities and choose one
        // on the next recursive call, we pass in i + 1 to represent that we're now picking
        // the "next" digit, as well as our current letter combination
        for (let j = 0; j < letterCombinations.length; ++j){
            search(i+1, cur + letterCombinations[j])
        }
    }
    search(0, "")
    return res
};