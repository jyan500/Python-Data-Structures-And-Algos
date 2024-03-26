/*
Neetcode solution:
Time Complexity: O(n*(2^n))
Space Complexity: O(N)
You don't need to pass in substrings within the recursion,
the key is that you can do the recursion with only one loop (instead of two like in my original solution),
and just pass in the index of the next character after our partition into the next recursive call.

example execution (not the entire recursive stack):
s = "aabcba"

1st recursive call
i = 0
j is also 0
cur = []
isPalindrome(s[0:1]) ("a") is true

So our first partition can be made on "a"
search(0+1, ["a"])

2nd recursive call
i = 1
j = 1
cur = ["a"]
isPalindrome(s[1:2]) ("a") is true 

2nd partition can be made on "a",
search(1+1, ["a", "a"])

3rd recursive call
i = 2
j = 2
cur = ["a", "a"]
j = 2, isPalindrome(s[2:3]) is false ("b") , so next iteration
j = 3, isPalindrome(s[2:4]) is false ("bc"), so next iteration
j = 4, isPalindrome(s[2:5]) is true ("bcb")

we need to pass in j = 5 to our next call
cur = ["a", "a", "bcb"]
search(5, ["a", "a", "bcb"])

4th recursive call
i = 5
j = 5
cur = ["a", "a", "bcb"]

j = 5, isPalindrome(s[5:6]) is true ("a")
cur = ["a", "a", "bcb", "a"]
search(6, ["a","a","bcb", "a"])

5th recursive call
here j = 6 which is >= s.length, so we just 
push ["a", "a", "bcb", "a"] to our res

backtracking to 4th call
we reach the end of the string, so there's nothing left to do here

backtracking to 3rd call
We were at this iteration of the loop, where i = 2 and j = 4
j = 4, isPalindrome(s[2:5]) is true ("bcb")
j = 5, isPalindrome(s[2:6]) is false ("bcba")

nothing left to do since we've reached the end of the string

backtracking to 2nd call

were at this iteration of the loop, where i = 1 and j = 1
j = 1 isPalindrome(s[1:2]) ("a") is true 
j = 2 isPalindrome(s[1:3]) ("aa") is true

cur = ["a", "aa"],
.....
you should be able to see the general execution of the recursion here as it backtracks and finds new cases.

*/
var partitionOptimized = function(s){
    let res = []
    var isPalindrome = function(substring){
        let l = 0
        let r = substring.length-1
        while (l <= r){
            if (substring[l] !== substring[r]){
                return false
            }
            ++l
            --r
        }
        return true
    }
    var search = function(i, cur){
        if (i >= s.length){
            res.push(cur)
            return
        }
        for (let j = i; j < s.length; ++j){
            let partition = s.slice(i, j+1)
            if (isPalindrome(partition)){
                search(j+1, [...cur, partition])
            }
        }
    }
    search(0, [])
    return res
}

/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    /*
    My initial solution:
    find all partitions
        -it seems that the max amount of partitions you can have 
        is the length of s - 1
        -you can also do 0 partitions (which is just string s)
        
    you can try all the different ways to partition starting from 0 to s.length-1
    the first partition that you make should result in a palindromic substring
    
    for example:
    a a b c b a
    
    0 partitions, aabcba, this is not palindromic
    1 partitions, a | abcba, this is palindromic, add to our list
                  aa | bcba, aa is palindromic, but bcba is not
                  aab | cba, not palindromic 
                  aabc | ba not palindromic
                  aabcb | a , aabcb is not palindromic, but a is
    2 partitions,
                  we can start by cutting at "a"
                  a | (abcba)
                  then in the second half, find another place to partition.
                  We can see that there's a subproblem here, because at every cut,
                  we need to decide where the next cut will be, which creates
                  a shorter subproblem each time. At each point, we only want to make a cut that would result in the current substring being palindromic
                    a | a | bcba
                    a | ab | cba X we wouldn't cut at "ab" because this isn't palindromic, so it automatically disqualifies the entire partition combination 
                    a | abc | ba X we would cut here either for the same reason
                    a | abcb | a X same here
    
    Time Complexity: O(N*(2^N))
    */
    let res = []
    
    var isPalindrome = function(s){
        l = 0
        r = s.length - 1
        while (l <= r){
            if (s[l] !== s[r]){
                return false
            }
            ++l
            --r
        }
        return true
    }
    var search = function(cutsRemaining, cur, substring){
        // if there's no more cuts remaining, and the current substring is 
        // palindromic (and also not an empty string), we can append
        // the current substring to our cur array and push it to res
        if (cutsRemaining === 0 && isPalindrome(substring) && substring !== ""){
            res.push([...cur, substring])
        }
        for (let i = 0; i < substring.length; ++i){
            let cut = substring.slice(0, i+1)
            // if cutting at this index results in a palindromic substring,
            // we then start a new subproblem, passing in the palindromic substring we just made, and then remaining substring into the next recursive call
            if (isPalindrome(cut)){
                search(cutsRemaining - 1, [...cur, substring.slice(0, i+1)], substring.slice(i+1, substring.length))
            }
        }
    }
    // initially, we can check whether the whole string is a palindrome (0 cuts)
    if (isPalindrome(s)){
        res.push([s])
    }
    // from here, we iterate based on the number of available partitions we can make
    for (let i = 1; i < s.length; ++i){
        search(i, [], s)
    }
    return res
};