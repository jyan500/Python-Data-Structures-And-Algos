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