/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    /*
    using O(1) memory
    the trick here is iterating the string in reverse. If we see a "#", that means
    we'd skip this character when evaluating. The algorithm involves figuring out when the "nextValidChar"
    is, and then continously checking if these characters across both strings are the same.

    within nextValidChar, the idea is that you want to track the amount of backspaces so far, and
    then based on this, continue decrementing until there are "no more" back spaces that can be used (when it's 0),
    and a non-back space character is reached
    An example:
    "dab##c#d" length = 8
    "ddb#a#" length = 6
    i starts at 7 i.e (8 - 1)
    j starts at 5 i.e (6 - 1)

    1st iteration of main while loop

    for nextValidChar(str, i = 7) 
    initially, backspaces = 0 and str[index] !== "#", so we'd break right away 

    for nextValidChar(str, j = 5) 
    j = 5
    backspaces = 0, and str[index] === "#", so increment backspaces by 1 and decrement index
    j = 4
    backspaces = 1, str[index] !== "#", decrement backspaces by 1 and decrement index
    j = 3
    backspaces = 0, str[index] === "#", increment backspaces by 1 and decrement index
    j = 2
    backspaces = 1, str[index] !== "#", decrement backspaces by 1 and decrement index
    j = 1
    backspaces = 0, str[index] !== "#", here we would break because there are no backspaces to use
    returns j = 1

    in the main while loop,
    s[7] === t[1], so we continue the main while loop
    decrement i and decrement j
    
    2nd iteration of main while loop
    i = 6
    j = 0
    nextValidChar(str, i = 6)
    initially, backspaces = 0 and str[index] === "#", increment backspaces and decrement index
    i = 5
    backspaces = 1, str[index] !== "#", decrement backspaces and decrement index
    i = 4
    backspaces = 0, str[index] === "#", increment backspaces and decrement index
    i = 3
    backspaces = 1, str[index] === "#", increment backspaces and decrement index
    i = 2
    backspaces = 2, str[index] !== "#", decrement backspaces and decrement index
    i = 1
    backspaces = 1, str[index] !== "#", decrement backspaces and decrement index
    i = 0
    backspaces = 0, str[index] !== "#", break since there are no more backspaces to use

    compares s[0] === t[0]
    
    the next iteration would go out of bounds, so break out of the while loop 
    
    returns true
    */
    var nextValidChar = function(str, index){
        let backspaces = 0
        while (index >= 0){
            // this would mean that in this index, there are no more backspace characters to use,
            // and this is not a backspace character, we'd just break right away
            if (backspaces === 0 && str[index] !== "#"){
                break
            }
            // if we see a pound, increment backspace by one
            else if (str[index] === "#"){
                backspaces++
            }
            // if we see a non-pound character, that means we've "used up" one backspace
            // to remove this character, so we decrement the amount of backspaces
            else {
                backspaces--
            }
            index--
        }
        return index
    }
    let i = s.length-1
    let j = t.length-1
    // if one of these strings goes out of bounds, we return false on the charS !== charT solution
    // which is why the loop condition is OR instead of AND
    while (i >= 0 || j >= 0) {
        i = nextValidChar(s, i)
        j = nextValidChar(t, j)
        let charS = i >= 0 ? s[i] : ""
        let charT = j >= 0 ? t[j] : ""
        if (charS !== charT){
            return false
        }
        i--
        j--
    }
    return true
    /*
    using O(N+M) memory, two stacks solution
    keep one stack per string, whenever you see a "#",
    pop off the top of the stack. And after through both
    s and t, compare the stacks

    */
    // let stack1 = []
    // let stack2 = []
    // for (let i = 0; i < s.length; ++i){
    //     if (stack1.length > 0){
    //         if (s[i] === "#"){
    //             stack1.pop()
    //             continue
    //         }
    //     }
    //     if (s[i] !== "#"){
    //         stack1.push(s[i])
    //     }
    // }
    // for (let j = 0; j < t.length; ++j){
    //     if (stack2.length > 0){
    //         if (t[j] === "#"){
    //             stack2.pop()
    //             continue
    //         }
    //     }
    //     if (t[j] !== "#"){
    //         stack2.push(t[j])
    //     }
    // }
    // return stack1.join("") === stack2.join("")
};