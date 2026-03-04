/**
 * @param {string} s
 * @return {boolean}
 */
class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    checkValidString(s) {
        /*
        3/3/2026
        (From Below)
        Time: O(N^2), if the entire string was * values,
        for each character, we'd need to consider two possibilities for each "*" character 
        so for example, ****, each character has two possibilities, so the total is 2 * 2 * 2 * 2 = 16,
        which is the same as 4^2. This indicates the amount of subproblems that we'd need to solve.
        
        Space: O(N^2), since along with each index, we're storing the current string configuration of our stack,
        similar to a 2-D DP problem.

        First instinct here is backtracking
        when you get to an asterisk character, it branches into three different possibilities

        recur(i+1, cur + [")"])
        recur(i+1, cur + ["("])
        # treat current character as an empty string and continue
        recur(i+1, cur)

        once you reach the last character, run the is valid parenthesis algorithm
        on this set of characters to see if its valid

        Rather than waiting until we reach the end to figure out whether we have
        a valid combination,
        keep track of the opening braces we have so far. Whenever we match an opening with a closing,
        we decrement the opening braces amount.
        However, if the opening braces amount becomes negative, that means there are too many
        closing braces, so this is not valid.
        
        If the num open === 0, this is valid, we'd check this in our base case once we've recurred
        through the whole string.

        To optimize, we need to cache at at a given i, and the number of opening braces left,
        can we create a valid parenthesis string? true/false
        */
        let N = s.length
        let memo = {}
        function search(i, numOpen){
            /* 
            if there are too many closing braces, we have to terminate early.
            For example, what if you had a string of only closing braces? 

            ")))"

            The number of opening braces is technically zero 
            since we never found any opening braces, but we wouldn't want to return
            the numOpen === 0, as we know there weren't any opening braces to begin with.
            this statement prevents this false positive!
            */
            let key = `${i},${numOpen}`
            if (numOpen < 0){
                return false
            }
            if (i >= N){
                return numOpen === 0
            }
            if (key in memo){
                return memo[key]
            }
            let flag = false
            if (s[i] === "(" || s[i] === ")"){
                memo[key] = search(i+1, s[i] === ")" ? numOpen - 1 : numOpen + 1)
                return memo[key]
            }
            const addClosing = search(i+1, numOpen-1)
            const addOpening = search(i+1, numOpen+1)
            const ignore = search(i+1, numOpen)
            memo[key] = addClosing || addOpening || ignore
            return memo[key]
        }
        return search(0, 0)
    }
}

/* 
    Note this is listed as a "greedy" problem, but personally find this much easier 
    to solve using Top Down Memoization, so moving this into the 2-D DP section instead.
    Top Down Solution

    Time: O(N^2), if the entire string was * values,
    for each character, we'd need to consider two possibilities for each "*" character 
    so for example, ****, each character has two possibilities, so the total is 2 * 2 * 2 * 2 = 16,
    which is the same as 4^2. This indicates the amount of subproblems that we'd need to solve.
    
    Space: O(N^2), since along with each index, we're storing the current string configuration of our stack,
    similar to a 2-D DP problem.

    Approach:
    1) We keep a "stack" (stored as a string for memoization purposes), where 
    we add onto the stack whenever we see a "(" and increment i to go onto the next string
    2) However, if we see a ")"
        and the stack length > 0, we check if the top of the stack === ")", if so 
        we "pop" by passing in the stack without the top element onto the next recursive call.
    3) If we see a "*",
    this means that we need to handle three cases,
    where we treat "*" as an opening brace, as a closing brace, or we just skip this character entirely
    and increment i and pass in the existing stack without any changes.

    Base case:
    if we've reached the end of the string, and our stack is empty, this means that 
    for each opening brace, there was a closing brace, so we've "cancelled" everything out, return true

    The trick with this problem is recognizing where to apply memoization. You can see there's an 
    "isValid" variable on the outside of the if blocks, and then the result of each recursive call
    is set to isValid. Then at the bottom, we then set the memo key to "isValid". The reason is that we have to evaluate all the possibilities before
    setting it to our memoization dict, otherwise, we might end up setting the value "too early"
    and end up returning a false positive in the statement that checks whether the key is in the memo.

    Another way of handling the recursion is instead of tracking the whole stack in memory, we can keep track of
    how many "opening" braces we have as the second parameter. And then if we encounter a closing brace, we then decrement the amount of 
    opening braces

*/

var checkValidString = function(s){
    let N = s.length
    let memo = {}
    var search = function(i, numOpening){
        if (i >= N){
            return numOpening === 0
        }
        if (`${i},${numOpening}` in memo){
            return memo[`${i},${numOpening}`]
        }
        let isValid = false
        if (s[i] === "*"){
            let left = search(i+1, numOpening+1)
            let empty = search(i+1, numOpening)
            let right = false
            if (numOpening > 0){
                right = search(i+1, numOpening-1) 
            } 
            isValid = left || empty || right
        }
        if (s[i] === "("){
            isValid = search(i+1, numOpening+1)
        }
        if (s[i] === ")"){
            if (numOpening > 0){
                isValid = search(i+1, numOpening-1)
            }
        }
        memo[`${i},${numOpening}`] = isValid
        return memo[`${i},${numOpening}`]
    }
    return search(0, 0)
}

var checkValidString = function(s) {
    let N = s.length
    let memo = {}
    var search = function(i, cur){
        if (i >= N){
            return cur.length === 0
        }
        if (`${i},${cur}` in memo){
            return memo[`${i},${cur}`]
        }
        let isValid = false
        if (s[i] === "*"){
            let left = search(i+1, cur + "(")
            let right = false
            // treat as an empty string, so just move onto the next character
            let empty = search(i+1, cur)
            if (cur.length > 0){
                if (cur[cur.length-1] === "("){
                    right = search(i+1, cur.slice(0, cur.length-1))
                }
            }
            isValid = left || empty || right   
        }
        if (s[i] === "("){
            isValid = search(i+1, cur + "(")     
        }
        if (s[i] === ")"){
            if (cur.length > 0){
                if (cur[cur.length-1] === "("){
                    isValid = search(i+1, cur.slice(0, cur.length-1))
                }
            }
        }
        memo[`${i},${cur}`] = isValid
        return memo[`${i},${cur}`]
    }
    return search(0, "")
};