class Solution {
    /**
     * @param {string} a
     * @param {string} b
     * @return {string}
     */
    addBinary(a, b) {
        /* 
        similar to add two numbers, except since we're in binary and not base 10,
        if the sum of two digits >= 2, we carryover 1, and set the current digit to sum - 2

        if one of the numbers is smaller than the other, we pad zeroes at the start
        */
        let aLength = a.length
        let bLength = b.length
        let newA = a
        let newB = b
        let longest = Math.max(aLength, bLength)
        if (aLength < bLength){
            newA = a.padStart(bLength, "0")
        }
        else if (aLength > bLength){
            newB = b.padStart(aLength, "0")
        }
        let carryover = "0"
        let output = []
        for (let i = longest-1; i >= 0; --i){
            let sum = Number(newA[i]) + Number(newB[i]) + Number(carryover)
            if (sum >= 2){
                carryover = "1"
                // append it to the front so the number doesn't come out in reverse order
                output.unshift((sum-2).toString())
            }
            else {
                carryover = "0"
                output.unshift(sum.toString())
            }
        }
        return carryover === "1" ? carryover + output.join("") : output.join("")
    }
}
