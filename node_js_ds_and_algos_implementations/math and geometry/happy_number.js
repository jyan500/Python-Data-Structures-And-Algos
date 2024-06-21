/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    /*
    one trick of this problem is that for numbers
    that aren't happy, if you repeatedly take the sum of squares for each digit, it'll eventually loop backwards to 
    a value that you've seen already, which indicates that it's
    not possible to get any other values. For example:
    2
    4
    16
    1^2+6^2 = 37
    3^2+7^2=9+49=58
    5^2+8^2=25+64=89
    8^2+9^2=64+81=145
    1^2+4^2+5^2=1+16+25=42
    4^2+2^2=20
    2*2 = 4
    
    We've already seen 4, so we know that this cycle of numbers
    will repeat itself.
    Set()
    while true
        if number === 1
            return true
        else
            take each digit, square it, and add the result, together, and then set to x. 
            add x to set()
            
    Therefore, we can use a Set and check whether we've already
    seen the result. If so, we break out of the loop

    Time Complexity: O(KLogN), where k is the number of iterations before terminating, floor(LogN) determines the number of digits
    in the input number N

    For example, if looping through all digits to get sum, we can only get up to floor(LogN) iterations since
    that is the max amount of digits of the current number
    Space: O(LogN), we're storing the unique results for input number N 

    https://math.stackexchange.com/questions/1384917/relation-between-number-of-digits-of-a-number-and-its-logarithm#:~:text=Assuming%20the%20logarithm%20is%20in,of%20digits%20in%20that%20number.&text=The%20number%20of%20decimal%20digits,log10N%E2%8C%8B%2B1.&text=Log%20of%20a%20number%20returns%20approximately%20the%20number%20of%20digits.
    https://stackoverflow.com/questions/58977656/how-to-understand-time-complexity-of-happy-number-problem-solution-from-leetcode
    */
    let visited = new Set()
    while (true){
        if (n === 1){
            return true
        }
        else {
            let digits = n
            let sum = 0
            // for (let i = 0; i < digits.length; ++i){
            //     sum += (parseInt(digits[i])**2)
            // }
            // you can get the individual digits like so, so you don't need to convert the number to a string
            while (digits !== 0){
                // get the last digit of the number starting from the one's place
                let digit = digits % 10
                sum += (digit ** 2)
                // advance to the next digit (up a tenth's place) using integer division
                digits = Math.floor(digits/10) 
            }
            // if we've already seen this sum, 
            // this means we're going to cycle through
            // the same results over and over, return false
            if (visited.has(sum)){
                return false
            }
            visited.add(sum)
            n = sum
        }
    }
};