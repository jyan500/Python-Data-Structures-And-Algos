class Solution {
    /*
    Revisited 7/7/2026
    Cleaner solution using math.trunc to always round the number closer to 0 if its a decimal
    (regardless of whether its positive or negative)
    */
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack = []
        let operators = ["+", "-", "/", "*"]
        for (let i = 0; i < tokens.length; ++i){
            if (operators.includes(tokens[i])){
                let num1 = stack.pop()
                let num2 = stack.pop()
                if (tokens[i] === "+"){
                    stack.push(num2 + num1)
                }
                if (tokens[i] === "-"){
                    stack.push(num2 - num1)
                }
                if (tokens[i] === "/"){
                    // remove the decimal portion with Math.trunc and moves the number
                    // closer to 0
                    stack.push(Math.trunc(num2/num1))    
                }
                if (tokens[i] === "*"){
                   stack.push(num2 * num1) 
                }
            }
            else {
                stack.push(Number(tokens[i]))
            }
        }
        return stack[0]
    }
}

/**
 * @param {string[]} tokens
 * @return {number}
 */
// https://leetcode.com/problems/evaluate-reverse-polish-notation/
var evalRPN = function(tokens) {
    let stack = []
    for (let i = 0; i < tokens.length; ++i){
        console.log("tokens[i]: ", tokens[i])
        console.log("stack: ", stack)
        switch (tokens[i]){
            case "+":
                second = stack.pop()
                first = stack.pop()
                stack.push(first+second)
                break
            case "-":
                second = stack.pop()
                first = stack.pop()
                stack.push(first-second)
                break
            case "/":
                second = stack.pop()
                first = stack.pop()
                quotient = first/second
                // note that if a negative decimal, we want to round closer to 0, so we'd need to do math.ceiling
                // if its a positive decimal, we'd do math.floor
                res = quotient > 0 ? Math.floor(first/second) : Math.ceil(first/second)
                stack.push(res)
                break
            case "*":
                second = stack.pop()
                first = stack.pop()
                stack.push(first * second)
                break
            default:
                stack.push(parseInt(tokens[i]))
                break
        }
    }
    return stack[0]
};