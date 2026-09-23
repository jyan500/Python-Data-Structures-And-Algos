class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations) {
        /* 
        stack problem
        [1,2,+]
        look at the last two, add them together and push (without popping out)
        [1, 2, 3, "C"]
        [1, 2], invalidate the previous score (pop out 3)
        [1, 2, 5, C], double the previous score => 10
        [1,2,5,10]
        sum together to get 18
        */
        let stack = []
        for (let i = 0; i < operations.length; ++i){
            if (stack.length){
                // there should always be at least two numbers on the stack before "+"
                if (operations[i] === "+"){
                    stack.push(stack[stack.length-1] + stack[stack.length-2])
                }
                else if (operations[i] === "C"){
                    stack.pop()
                }
                else if (operations[i] === "D"){
                    stack.push(stack[stack.length-1] * 2)
                } 
                else {
                    stack.push(Number(operations[i]))
                }
                continue
            }
            else {
                stack.push(Number(operations[i]))
            }
        }
        return stack.reduce((acc, total) => acc + total, 0)

    }
