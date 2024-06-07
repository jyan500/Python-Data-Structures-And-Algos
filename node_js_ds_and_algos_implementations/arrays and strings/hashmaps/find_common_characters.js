/**
 * @param {string[]} words
 * @return {string[]}
 */

/*
Approach:
to find the common characters that are found in all strings in the word list
1) For the first word in the word list, get the counts of all characters and store in "commonCounter"
2) For each word after the first word in the word list, initialize a counter which has all
the same characters as in "commonCounter", except the counts are set to 0, called "currentCounter"
3) Get the counts of each character and store in counter
4) Key Step: loop through all characters in the currentCounter, and then take the MIN between
the counts of the given character in currentCounter, and commonCounter. The reason we take the MIN is because
we want to ensure that in edge cases like "cool" and "cole", where only one "O" exists for one of the words,
we still accept the one "O", i.e MIN(2, 1)
5) At the end, loop through all characters in commonCounter and append to the list N times, where N is the character
count in commonCounter

Time Complexity: O(N^2), since for each word in words, we need to compare each subsequent word after the first 
word to the first word
Space: O(26)
*/
var commonChars = function(words) {
    let commonCounter = {}
    for (let i = 0; i < words[0].length; ++i){
        if (!(words[0][i] in commonCounter)){
            commonCounter[words[0][i]] = 1
        }
        else {
            ++commonCounter[words[0][i]]
        }
    }
    for (let i = 1; i < words.length; ++i){
        let currentCounter = {...commonCounter}
        for (let key of Object.keys(currentCounter)){
            currentCounter[key] = 0
        }
        for (let char of words[i]){
            if (!(char in currentCounter)){
                currentCounter[char] = 1
            }
            else {
                ++currentCounter[char]
            }
        }
        for (let key of Object.keys(currentCounter)){
            if (key in commonCounter){
                commonCounter[key] = Math.min(commonCounter[key], currentCounter[key])
            }
        }
    }
    let res = []
    for (let key of Object.keys(commonCounter)){
        for (i = 0; i < commonCounter[key]; ++i){
            res.push(key)
        }
    }
    return res
    
    
};