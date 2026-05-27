class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        /*
        given n,
        you need n opening parenthesis and n closing parenthesis present
        to be considered a valid string of parenthesis

        if you add an opening
        (
         in the next spot, you can add either another opening or closing 

        if there are more opening braces than closing braces (and there are still closing braces available), 
        you can add a closing brace

        example execution:
        n = 3
        ((())) is the first one that's found (since we continually pick opening braces, then closing braces)
        (( - in this case, we have 2 openings and 0 closings, so the amount of openings > amount of closings, so we can add a closing brace
        (() - now at this step, we have 2 openings and 1 closing, we have the choice of adding an opening brace, or a closing brace,

      (()( - adds opening, this is valid -> branches into another recursion tree
      (()) - adds closing, this is also valid -> branches into another recursion tree
        */

        let res = []
        const search = (numOpen, numClose, cur) => {
            if (numOpen === n && numClose === n){
                res.push(cur.join(""))
                return
            }
            // always try adding an opening brace first
            if (numOpen < n){
                search(numOpen+1, numClose, [...cur, "("])
            }
            // add closing if the amount of opening braces is greater than the amount of closing
            // and there are still closing braces
            if (numOpen > numClose && numClose < n){
                search(numOpen, numClose+1, [...cur, ")"])
            }
        }
        search(0,0, [])
        return res

    }
}

/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    /*
    using backtracking
    given you have n pairs of parenthesis, you will have n*2 total,
    with n opening braces, and n closing braces
    
    decision tree
    you always start by using an opening brace
    (
    
    at this point, you can either:
    1) add another opening brace, subtract one from total num of opening braces
    2) add a closing brace, subtract one from total num of closing braces
    
        (
     ()   ((
     
     Note at with the left side, we can't add another closing brace since we've 
     created a valid pair so far, so we can only add an opening brace
     
        (
     ()   ((
     
   ()(  (() (((
    
    Note on the right most side (((, we've run out of opening braces, so we must pick closing braces only
    
    at a given recursive call, we can tell whether we have 2 options (add opening or closing), or 1 option (adding only opening),
    if we keep a track of a stack. Whenever we add an opening brace, we add to the stack. If we add a closing brace,
    instead of adding to the top of the stack, we pop off the stack. 
    
    Exponential Time Complexity
    */
    let res = []
    const helper = (cur, numLeft, numRight, stack) => {
        if (numLeft <= 0 && numRight <= 0){
            res.push(cur)
            return
        }
        if (stack.length > 0){   
            if (stack[stack.length-1] === "("){
                if (numLeft > 0){
                    helper(cur + "(", numLeft - 1, numRight, stack.concat("("))
                }
                if (numRight > 0){
                    helper(cur + ")", numLeft, numRight - 1, stack.splice(1, stack.length-1))
                }
            }
        }
        else {
            if (numLeft > 0){
                helper(cur + "(", numLeft - 1, numRight, stack.concat("("))
            }
        }
        
    }
    // we always start with an opening brace no matter what, otherwise the entire string would be considered invalid
    helper("(", n-1, n, ["("])
    return res
};