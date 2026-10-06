class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    minRemoveToMakeValid(s) {
        /* 
        use a stack, keeping track of the element
        and its index
        apply the valid parenthesis algorithm so that
        we pop out valid pairs of parenthesis
        the only elements left in the stack are the invalid ones
        that need to be removed
        Time: O(2N) (2 separate loops and set conversion)
        Space: O(N) for the copy of the string with invalid parens removed
        */
        let stack = []
        for (let i = 0; i < s.length; ++i){
            if (stack.length > 0 && s[i] === ")" && stack[stack.length-1][0] === "("){
                stack.pop()
                continue
            }
            if (s[i] === "(" || s[i] === ")"){
                stack.push([s[i], i])
            }
        }
        let indices = stack.reduce((acc, obj) => {
            acc.add(obj[1])
            return acc
        }, new Set())
        let res = [] 
        for (let i = 0; i < s.length; ++i){
            if (!indices.has(i)){
                res.push(s[i])
            }
        }
        return res.join("")
    }
}
