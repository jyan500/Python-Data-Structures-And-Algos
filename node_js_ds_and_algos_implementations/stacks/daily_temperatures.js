class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        /* 
        Revisited 9/9/2026
        Monotonic Stack 
        Anytime we get a temperature that's greater than the last, we pop off
        the stack, so the stack is strictly decreasing in value
        Also store the index of the temperature on the stack so we know
        the distance of the indices where the temperature is now greater

        i = 0
        temps = [0,0,0,0,0,0,0]
        stack = [[30, 0]]

        i = 1
        38 > 30, so pop off the stack
        stack = [[38, 1]]
        temps = [1,0,0,0,0,0,0]

        i = 2
        30 < 38, so append
        stack = [[38,1], [30,2]]
        temps = [1,0,0,0,0,0,0]

        i = 3
        36 > 30, pop off the stack
        stack = [[38,1], [36,3]]
        temps = [1,0,1,0,0,0,0]

        i = 4
        35 < 36, append
        stack = [[38,1],[36,3],[35,4]]
        temps = [1,0,1,0,0,0,0]

        i = 5
        40 > 35, pop off
        this time, we continue popping off since it's also greater than 36
        and also 38 too
        so we have to set the indices for multiple
        distance between [40,5] and [35,4] is 1
        distance between [40,5] and [36,3] is 2
        distance between [40,5] and [38,1] is 4
        stack = [[40,5]]
        temps = [1,4,1,2,1,0,0]

        stack = [[40,5],[28,6]]
        Finished iteration, return temps
        note that the stack is not empty because there are no greater temps reached
        for indices 5 and 6

        Time: O(N)
        Space: O(N)
        */
        let temps = Array(temperatures.length).fill(0)
        let stack = []
        for (let i = 0; i < temperatures.length; ++i){
            while (stack.length && stack[stack.length-1][0] < temperatures[i]){
                let [_, index] = stack.pop()
                temps[index] = i - index
            }
            stack.push([temperatures[i], i])
        }
        return temps
    }
}

/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
 /*
 O(N) Time
 O(N) Space

 Key Concepts:
 Using a stack and saving the element as well as its index
 to see what the difference in indexes is

 */
var dailyTemperatures = function(temperatures) {
    /*
    
    */
    let res = Array(temperatures.length).fill(0)
    let stack = []
    for (let i = 0; i < temperatures.length; ++i){
        if (stack.length > 0){
            while (stack.length > 0){
                let top = stack[stack.length-1]
                let [topTemp, topIndex] = stack[stack.length-1].split(",")
                if (topTemp < temperatures[i]){
                    let diff = i - topIndex
                    res[topIndex] = diff
                    stack.pop()
                }
                else {
                    break
                }
            }
        }
        const pair = `${temperatures[i]},${i}`
        stack.push(pair)
    }
    return res
};