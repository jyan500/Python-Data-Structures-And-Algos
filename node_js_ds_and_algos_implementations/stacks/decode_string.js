class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    decodeString(s) {
        /*
        4/28/2026
        stack problem
        there is always a number followed by a bracket
        but the number can be greater than 1 so we have to construct it
        then when we encounter a bracket, push the number to the stack
        if it's a letter, push to the stack
        if it's a closing brace, pop out twice, the first element is the letter
        and the second is the number, where you multiply the letter by the number
        (i.3 3 * e = eee)
        and push it back on the stack 
        */
        let curNumber = 0 
        let stack = []
        for (let i = 0; i < s.length; ++i){
            console.log("stack: ", stack)
            // if it's a digit, multiply the current by 10 and add the digit
            // i.e if 201, the first digit 2 is (0*10) + 2 = 2, then (2*10) + 0 = 20, then (20*10) + 1
            // which is 201
            const isDigit = (element) => !isNaN(Number(element))
            if (isDigit(s[i])){
                curNumber = (curNumber * 10) + Number(s[i])
            }
            // if opening brace, push the current number to the stack
            else if (s[i] === "["){
                stack.push(curNumber)
                curNumber = 0
            } 
            // while it's not a number, continue popping out of the stack, combine the letter combinations
            // together
            else if (s[i] === "]"){
                let letters = []
                while (!isDigit(stack[stack.length-1])){
                    let letter = stack.pop()
                    // append to the beginning
                    letters.unshift(letter)
                }
                let number = stack.pop()
                stack.push(letters.join("").repeat(number))
            }
            // if it's not a number, closing or opening brace, it must be a letter
            else {
                stack.push(s[i])
            }
        }
        return stack.join("")
    }
}
