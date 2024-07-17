/**
 * @param {string} text
 * @return {number}
 */
/*
Approach:

get counts of all chars in text
s = "balloon"
total = 0 
while (true)
    found = 0
    for each char in s
        if char in counter and counter[char] > 0
            decrement counter[char]
            increment found
        else
            break, because we can't form the word balloon if we can't find all chars
    // if we've found all the characters for "balloon", increment total by 1
    if found === s.length
        increment total
    else
        break
return total

O(N^2) time
O(N) space

*/
var maxNumberOfBalloons = function(text) {
    let counter = {}
    for (let c of text){
        if (c in counter){
            ++counter[c]
        }
        else {
            counter[c] = 1
        }
    }
    let count = 0
    let s = "balloon"

    while (true){
        let found = 0
        for (let c of s){
            if (c in counter && counter[c] > 0){
                counter[c]--
                ++found
            }
            else {
                break
            }
        }
        if (found === s.length){
            ++count
        }
        else {
            break
        }
    }
    return count
};