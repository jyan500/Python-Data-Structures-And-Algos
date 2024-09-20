/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2) {
    /*
    two pointers solution O(N) O(1) Time
    track both the current index within the word array,
    as well as the current char within word[index]
    
    the idea is that you continue comparing chars within each word until you reach 
    the end of one word. And then you would increment the current index within the word array,
    and then reset the index that represents the current within word[index] to be 0
    
    Neetcode: https://youtu.be/ejBwc2oE7ck
    (his solution is cleaner but I've written the logic here to be more verbose but straightforward to follow)
    */
    let w1Index = 0
    let w2Index = 0
    let i = 0
    let j = 0
    while (w1Index < word1.length && w2Index < word2.length){
        let w1 = word1[w1Index]
        let w2 = word2[w2Index]
        // if you're able to continue the characters within both words, continue to do so
        // if the characters are not equal, return false
        if (i < w1.length && j < w2.length){
            if (w1[i] === w2[j]){
                ++i
                ++j
            }
            else {
                return false
            }
        }
        // if you reached the end of one word within the array but not the other,
        // move the index to the next word of the array, and reset the inner pointer to be 0
        // so it starts at the beginning of the next word
        else if (i < w1.length && j === w2.length){
            w2Index++
            j = 0
        }
        else if (i === w1.length && j < w2.length){
            w1Index++
            i = 0
        }
        // in the case BOTH indices have reached the end of the word,
        // perform the same operation as above but for both the indices representing each word 
        // in the array (w1 Index and w2 Index), and each index that represents the character within each word (i , j)
        else if (i === w1.length && j === w2.length){
            w1Index++
            w2Index++
            i = 0
            j = 0
        }
    }
    // if both words are fully iterated, that means the word arrays are equal. If one of the arrays is still not fully iterated,
    // that means the word arrays are not equal
    return w1Index === word1.length && w2Index === word2.length
};