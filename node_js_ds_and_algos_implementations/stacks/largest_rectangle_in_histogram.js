/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    /*
    what's the biggest area we could make as we traverse?
    
    Neetcode:
    1) Use a stack, track the index and the height. 
    2) Within the stack, keep only heights that are strictly increasing. If it's not strictly 
    increasing, that means the area cannot be extended further due to them smaller height,
    3) If so, calculate the width between the current index and the index of the height
    that was too big, and then multiply the height to get the area. We then pop off the stack
    We then add the current element, but record the index of the LAST element that we just popped from the stack
    instead of the current index and also the height. We do this because the current height is smaller than the previous, so we can start calculating the width from that index.
    i.e 
    
    for example, if we popped the height of 2 here
    |
    | |
    2 1,
    starting 1 back at index 0 would be the equivalent of:
    
    | |
    1 1
    (the height of 1 is "included" in the height of 2)
    
    4) Also keep track of the max area we've found so far
    5) If there are any elements left on the stack, that means they're strictly increasing,
    and still need to be computed.
    
          |   
        | | 
        | |
        | |   |
    |   | | | |
    | | | | | |
    2 1 5 6 2 3
    
    i = 0
    stack = [{height: 2, index: 0}]
    
    i = 1
    See that the current height of 1 is < than the top of stack height, 2
    Calculate the width (1 - 0) * height of 2 = area of 2
    max Area = 2
    Add the current height to the stack, and use the index of the element we just popped off
    stack = [{height: 1, index: 0}]
    
    i = 2
    Add the current height to the stack because it's greater than the height at the top of the stack
    stack = [{height: 1, index: 0}, {height: 5, index: 2}]
    
    i = 3
    Add the current height to the stack because it's greater than the height at the top of the stack
    stack = [{height: 1, index: 0}, {height: 5, index: 2}, {height: 6, index: 3}]
    
    i = 4
    
    See that the current height of 2 is less than the top of stack height, 6
    Calculate the width (4-3) * height of 6 = 6
    max(2, 6) = 6, so max Area is now 6   
    Pop off the stack
    stack = [{height: 1, index: 0}, {height: 5, index: 2}]
    
    See that the current height of 2 is less than the top of stack height, 5
    Calculate the width (4-2) * height of 5 = 10
    max (6, 10) = 10, so max Area is now 10    
    Pop off stack
    stack = [{height: 1, index: 0}]
    
    We can now add the current element to the stack since it's height is greater,
    use the index of the last element that we just popped off
    stack = [{height: 1, index: 0}, {height: 2, index: 2}]
    
    i = 5
    
    3 > 2, so add to the top of the stack
    stack = [{height: 1, index: 0}, {height: 2, index: 2}, {height: 3, index: 5}]
    
    i = 6
    we reached the end of the histogram, but there are still elements left in our stack
    
    Calculate the areas of each by taking (i - element.index) * height of element
    
    (6 - 5) * 3 = 3 
    (6 - 2) * 2 = 8
    (6 - 0) * 1 = 6
    
    None of these areas is greater than max, so the max area is still 10
    */
    let i = 0
    let maxArea = 0
    let stack = []
    while (i < heights.length){
        if (stack.length > 0 && stack[stack.length-1].height > heights[i]){
        	// we keep track of the last element that we popped off the stack
        	// so that we can set the index of the current element to the index of this
        	// last element below after the while loop is done
            let prev = stack[stack.length-1]
            while (stack.length > 0 && stack[stack.length-1].height > heights[i]){
                const {height, index} = stack[stack.length-1]
                let width = i - index
                maxArea = Math.max(height * width, maxArea)
                prev = stack.pop()
            }
            stack.push({height: heights[i], index: prev.index})
        }
        else {
            stack.push({height: heights[i], index: i})
        }
        ++i
    }
    // if there are any elements left in the stack, calculate the max area
    for (let j = 0; j < stack.length; ++j){
        let width = i - stack[j].index
        let height = stack[j].height
        maxArea = Math.max(width*height, maxArea)
    }
    return maxArea
};