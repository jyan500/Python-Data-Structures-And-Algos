class Solution {
    /**
     * @param {string} str1
     * @param {string} str2
     * @return {string}
     */
    gcdOfStrings(str1, str2) {
        /*
        Find the GCD between the two string lengths
        compare the window size of GCD to both strings to see if the window actually matches

        To find the GCD:
        take the longer number and mod by the shorter number
        then recursively, pass in the shorter number as the longer number, and the remainder as the shorter number

        the base case is where the remainder becomes 0, then just return the shorter number

        for example
        str1="TAUXXTAUXXTAUXXTAUXXTAUXX"
        str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
        longer = 45 shorter = 25
        45 % 25 = 20
        gcd(20, 15)

        20 % 15 = 5
        gcd(15, 5)

        15 % 5 = 0
        remainder is 0, so we return the smaller number 5

        Therefore, we take the window of 5 since we know this is the greatest divisor we can
        have between these two numbers, and check whether the values on both sides
        will match

        O(N) Time (note that finding the GCD itself is only OLog(min(A,B)))
        O(K) Space since we're creating windows of size K where K is the gcd
        */
        let longer = str1.length >= str2.length ? str1 : str2
        let shorter = str1 === longer ? str2 : str1

        function getGcd(long, short){
            let remainder = long % short
            if (remainder === 0){
                return short
            }
            return getGcd(short, remainder)
        }

        let gcd = getGcd(longer.length, shorter.length)
        let window = shorter.slice(0, gcd)
        let j = 0
        while (j < longer.length){
            let window2 = longer.slice(j, j+gcd)
            if (window !== window2){
                return ""
            }
            j += window2.length
        }
        return window
    }
}
