/**
 * @param {string} s
 * @return {string}
 */
/* 
https://leetcode.com/problems/make-the-string-great/
O(N) Time O(N) Space
Similar to the valid parenthesis problem,
if the top of the stack is lowercase, but the current char is upper, pop the top of the stack,
so that character is removed, and the upper case character is not added to the stack.
*/
var makeGood = function(s) {
    let stack = []
    for (let char of s){
        if (stack.length > 0){
            let top = stack[stack.length-1]
            if (char.toLowerCase() === top.toLowerCase() && char != top){
                stack.pop()
                continue
            }
            
        }
        stack.push(char)

    }
    return stack.join("")
};