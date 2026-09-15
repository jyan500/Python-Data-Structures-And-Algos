class Solution {
    /**
     * @param {number} num
     * @return {string}
     */
    intToRoman(num) {
        /* 
        1) List out all rules (including subtractive rules)
        so the special cases for numbers that start with 4 or 9
        i.e M = 1000, but 900 = CM, etc
        2) starting from the largest rule, divide by the original number by that, then mod from the original number the rule val to continue parsing the next digit of the original number
        i.e 3
        */
        let res = []
        const rules = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000],
        ]
        for (let i = rules.length - 1; i >= 0; --i){
            const [sym, val] = rules[i]
            let count = Math.floor(num/val)
            if (count > 0){
                // for example, if 3000, and our rule is currently at 1000,
                // we repeat "M" three times
                for (let k = 0; k < count; ++k){
                    res.push(sym)
                }
                // reduce the num by the rule amount
                // i.e 3930 % 1000 = 930, so know we process 930
                num = num % val
            }
        }
        return res.join("")
    }
}
