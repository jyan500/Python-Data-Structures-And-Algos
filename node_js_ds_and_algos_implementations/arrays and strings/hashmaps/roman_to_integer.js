class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    romanToInt(s) {
        let map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        const isSubtraction = (cur, prev) => {
            return (
            (cur === "V" && prev === "I") || 
            (cur === "X" && prev === "I") || 
            (cur === "L" && prev === "X") ||
            (cur === "C" && prev === "X") ||
            (cur === "D" && prev === "C") || 
            (cur === "M" && prev === "C"))
        }

        let res = 0
        for (let i = 0; i < s.length; ++i){
            if (i > 0){
                if (isSubtraction(s[i], s[i-1])){
                    // if we hit one of the special cases where we need to subtract,
                    // we would take the last element we added and double it's value as 
                    // a negative number to "offset" what we added before, and also apply
                    // the subtraction effect
                    // for example, for IV, if we added I, that'd be 1
                    // So we'd subtract 2, -1, and then re-add V, which is 5, to
                    // get 4, which is the correct number for IV
                    res -= (map[s[i-1]]*2)
                }
            }
            res += map[s[i]]
        }
        return res
    }
}
