/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
/*
Approach:
2-D Dynamic Programming
https://www.youtube.com/watch?v=HAA8mgxlov8&t=371s&ab_channel=NeetCode

Recurrence Relation:

1) Defining what a "match" is
If we see a matching character or a "." (which is a wildcard that matches only one character),
AND we haven't reached the end of string S (i < M), which means there's more characters to match

this boolean is stored as a variable since it will be reused

match = (i < M) && (s[i] === p[j] || p[j] === ".")

2) recognizing how to handle * case:

the * means we match zero or more of the character one index to the left of the *
for example

s = aab
p = c*a*b

For c*, we would match zero or more of the character "c". In this case, 
we'd want to match zero chars since the corresponding character in string s (which is "a")
doesn't match with c

IF we still have at least characters we can match in P (j + 1 < N), and the next character (p[j+1]) is a *, we have two choices (which leads to the decision tree)
    a) Use the * character to see if we can match the current character (p[j]) with any future characters in S
        - Note that we only follow this recursive path IF the match boolean variable we defined is true
    b) Don't use the * character and increment j PAST the * (j+2)

3) 
IF there's a match (based on the match boolean variable),
    we can increment both i and j

else:
    return false, as this indicates there's no match

Base Cases:

If i >= M and j >= N, this means that we've matched every character in string P with string S, so
this is valid

However, if we've gone through all characters in P, and there are still characters in string S that haven't been
matched, this is not valid

The tricky case is realizing that just because j >= N (return false), doesn't mean that we should do
i >= M (return false), as there are cases where we may traverse all of string S, but there are still
characters in string P

for example:
S = a
P = a*b*

Here, we'd match a to a*, but after that, there are no more characters in S to match. However,
we can still continue down P, by matching zero characters on b*, 
even though we've already matched all of S already.

Time Complexity:
O(N*M), if we see a * character in P, it's possible that we try and iterate through all characters of S
to match zero or more chars of P
Space Complexity:
O(N*M)

*/
var isMatch = function(s, p) {
    let M = s.length
    let N = p.length
    let memo = {}
    var search = function(i, j){
        if (i >= M && j >= N){
            return true
        }
        if (j >= N){
            return false
        }
        if (`${i},${j}` in memo){
            return memo[`${i},${j}`]
        }
        let match = i < M && (s[i] === p[j] || p[j] === ".")
        if (j+1 < N && p[j+1] === "*"){
            memo[`${i},${j}`] = (match && search(i+1,j)) || search(i, j+2)
            return memo[`${i},${j}`]
        }
        if (match){
            memo[`${i},${j}`] = search(i+1,j+1)
            return memo[`${i},${j}`]
        }
        memo[`${i},${j}`] = false
        return memo[`${i},${j}`]
    }
    return search(0,0)
};