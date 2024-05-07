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