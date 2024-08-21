/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function(s) {
    /* 
    Optimized (see the python file for the full explanation, but the idea
    is that each time you see a closed bracket, it's either
    A) valid, and has a matching opening bracket before it
    B) needs to be fixed
    
    In the case of needing to be fixed, you can just transform it into an opening bracket
    to fix the string.
    
    Note that because we're not interested in finding out which exact indexes need to swap,
    only the AMOUNT of fixes necessary, this solution can work.
    
    you track two variables, currentOpen and numFixes.
    Each time you see an opening bracket, increment currentOpen
    Each time you see a closed bracket, you check if there's an opening bracket based on currentOpen.
    If currentOpen > 0 and it's a closed bracket, you can "spend" one opening bracket to match this closing brace, decrementing currentOpen
    However, if currentOpen === 0, this is an invalid closing bracket. So you'll need to change
    this to an opening brace as a "fix", and increment currentOpen by one.
    */
    let currentOpening = 0
    let numFixes = 0
    for (let c of s){
        if (c === "["){
            currentOpening++
        }
        else if (currentOpening > 0){
            currentOpening--
        }
        else {
            currentOpening++
            numFixes++
        }
    }
    return numFixes
    /*
    Brute Force solution:
    based on the number of opening and closing braces,
    calculate all different combinations of valid braces
    
    Iterate through all combinations, and then check to see which combination
    has the least differing amount of characters from the given string s, and find
    out how many characters are differing, and divide that by 2 (since one action accounts for two differing characters), that would give the answer.
    */
    // let combinations = new Set()
    // var dfs = function(numOpening, numClosing, cur){
    //     if (numOpening === 0 && numClosing === 0){
    //         combinations.add(cur)
    //     }
    //     if (numOpening > 0){
    //         dfs(numOpening-1, numClosing, cur + "[")
    //     }
    //     // can only put a closing brace IF there's less opening braces than closing,
    //     // so you'd need to add a closing brace to bring closer to balance,
    //     // OR there are no more opening braces and there are still closing braces left
    //     if (numOpening < numClosing || numOpening === 0 && numClosing > 0){
    //         dfs(numOpening, numClosing-1, cur +  "]")
    //     }
    // }
    // dfs(s.length/2, s.length/2, "")
    // let least = Number.POSITIVE_INFINITY
    // for (let word of combinations){
    //     let numDiffering = 0
    //     for (let i = 0; i < word.length; ++i){
    //         if (word[i] !== s[i]){
    //             ++numDiffering
    //         }
    //     }
    //     least = Math.min(numDiffering, least)
    // }
    // return least !== Number.POSITIVE_INFINITY ? least/2 : 0
};