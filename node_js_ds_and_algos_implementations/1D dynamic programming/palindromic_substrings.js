/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    /* 
    Similar to the other palindromic substring problems, 
    you perform an inner while loop that checks the indices going outwards from the starting point
    for odd length palindromes, l and r start at i
    for even length palindromes, l starts at i, and r starts at i + 1
    Time Complexity:
    O(N^2)
    */
    let N = s.length
    let numPalindromes = 0
    // from i = 0 ... N

    for (let i = 0; i < N; ++i){
        let l1 = i
        let r1 = i
        // check for odd length palindromes, each time s[l] === s[r] match,
        // this would be considered another palindromic substring, so increment
        while (l1 >= 0 && r1 <= N - 1){
            if (s[l1] !== s[r1]){
                break
            }
            --l1
            ++r1
            ++numPalindromes           
        }
        let l2 = i
        let r2 = i + 1
        // check for even length palindromes
        while (l2 >= 0 && r2 <= N - 1){
            if (s[l2] !== s[r2]){
                break
            }
            --l2
            ++r2
            ++numPalindromes
        }
    }
    return numPalindromes
};