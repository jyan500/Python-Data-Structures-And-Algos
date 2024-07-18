/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    /*
    sliding window
    Time: O(N)
    Space: O(1)
    */
    let l = 0
    let r = 0
    let max = Number.NEGATIVE_INFINITY
    let res = ""
    let currentWindow = num[0]
    while (l < num.length && r < num.length){
        // if the digits are equal and the length of the window is 3
        if (num[l] === num[r] && r - l + 1 === 3){
            // determine if the window is larger than the current max, if so update current max
            if (parseInt(currentWindow) > max){
                max = parseInt(currentWindow)
                res = currentWindow
            }
            // set the beginning of the next window to the next index so both l and r start at the next index
            // and set the current window to be just the character at the next index
            ++r
            l = r
            currentWindow = num[r]
            continue
        }
        // if the chars are equal, increment only the right pointer and add the next char to the current window 
        if (num[l] === num[r]){
            ++r
            currentWindow += num[r]
        }
        // if the chars are not equal, set the left pointer equal to where the right pointer is, so this will be
        // the start of the new window
        else if (num[l] !== num[r]){
            // set the beginning of the next window to the next index so both l and r start at the next index
            // and set the current window to be just the character at the next index
            l = r
            currentWindow = num[r]
        }
    }
    return res
    
};