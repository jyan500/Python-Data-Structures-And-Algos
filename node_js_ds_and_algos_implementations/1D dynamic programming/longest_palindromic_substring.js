class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    longestPalindrome(s) {
        // revisited 5/20/2026
        // for each character, set two pointers starting at given index
        // and move them outwards
        // for even length palindromes, start l = i, r = i + 1
        // for odd numbered, start l = i, r = i
        let curLength = 0
        let res = ""
        for (let i = 0; i < s.length; ++i){
            // find odd length
            let l1 = i
            let r1 = i
            while (l1 >= 0 && r1 < s.length && s[l1] === s[r1]){
                --l1
                ++r1
            }
            let l2 = i
            let r2 = i+1
            while (l2 >= 0 && r2 < s.length && s[l2] === s[r2]){
                --l2
                ++r2
            }
            let oddLength = r1-l1-1
            let evenLength = r2-l2-1
            if (oddLength > evenLength && oddLength > curLength){
                res = s.slice(l1+1,r1)
                curLength = oddLength
            }
            else if (oddLength < evenLength && evenLength > curLength) {
                res = s.slice(l2+1, r2)
                curLength = evenLength
            }
        }
        return res
    }
}

/**
 * @param {string} s
 * @return {string}
 */
/* 
Similar approach to length of longest palindromic substring, 
except this time you keep track of the left and right boundaries
once you've found a substring length that exceeds the max.

In the while loop, when exceeding the boundary, you have to shrink the boundary
back by 1 (adding one to the left, subtracting one from the right) since it would
"one too many" due to the structure of the loop

Time Complexity:
O(N^2)
Space:
O(1)
*/
var longestPalindrome = function(s) {
    let N = s.length
    if (N === 1){
        return s[0]
    }
    let maxCount = 0
    let maxIndices = []
    for (let i = 0; i < N; ++i){
        let l1 = i-1
        let r1 = i+1
        let oddCount = 1
        while (true){
            // if we extend past the boundaries, we need to add one back to the left
            // and subtract one back to the right to get the correct boundaries
            if (!(l1 >= 0 && r1 <= N - 1)){
                ++l1
                --r1
                break
            }
            // if we extend past a valid palindromic substring, we need to add one back to the left
            // and subtract one back to the right to get the correct boundaries
            if (s[l1] !== s[r1]){
                ++l1
                --r1
                break
            }
            oddCount += 2
            --l1
            ++r1
        }
        let l2 = i
        let r2 = i + 1
        let evenCount = 0
        while (true){
            if (!(l2 >= 0 && r2 <= N - 1)){
                ++l2
                --r2
                break
            }
            if (s[l2] !== s[r2]){
                ++l2
                --r2
                break    
            }
            evenCount += 2
            --l2
            ++r2
        }
        let indices = oddCount > evenCount ? [l1, r1] : [l2, r2]
        if (oddCount > maxCount){
            maxCount = oddCount
            maxIndices = indices
        }
        else if (evenCount > maxCount){
            maxCount = evenCount
            maxIndices = indices
        }
    }
    return s.slice(maxIndices[0], maxIndices[1]+1)
};