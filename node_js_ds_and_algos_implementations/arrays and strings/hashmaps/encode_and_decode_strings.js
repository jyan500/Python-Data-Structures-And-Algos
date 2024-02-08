/*
	Without using the split and join method, the approach is:
	1) Keep a hashmap that maps a dummy character to the actual string in the list. For example,
	if we map each string in the list to its index, then we can freely add whichever delimiter
	we want without having to worry about conflicts. 

	2) For encode, we return the string with each string in the list replaced with an index

	list = ["res", ";", "test with spaces", "a", "a", "a", "a", "a", "a", "a", "a"]
	11 items total

	gets mapped to 

	{0: "res", 1: ";", 2: "test with spaces", .... 10: "a"}

	and we return

	0;1;2;3;4;5;6;7;8;9;10;

	3) In our decode, we would keep two pointers, where we increment the right pointer until
	it reaches a ";" character, and then slice everything between the left and right pointer
	and treat that as the "index" to our hashmap. This allows us to retrieve the original string 
	in it's proper order and push to our result list. 

	We use two pointers because in instances of long lists, we need to account
	for multiple digit indices (i.e 10 and onwards)

	i = 0, j = 1
	We slice from 0 to 1 to get "0", and then we convert "0" back to integer, 
	and find this.map[0] to get "res", and push this back into our res list

	...

	This repeats up until index 23 (which is the last semicolon), where we slice between 21 and 23
	to get "10", which convert back to an integer, and find the last "a", to get our final result

	["res", ";", "test with spaces", "a", "a", "a", "a", "a", "a", "a", "a"]

	O(N) Time O(N) Space



*/
class Solution {
    constructor(){
        this.map = {}
    }
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = ""
        for (let i = 0; i < strs.length; ++i){
            this.map[i] = strs[i]
            res += `${i}${i < strs.length ? ";" : ""}`
        }
        return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i = 0
        let j = 0
        let res = []
        while (j < str.length){
            if (str[j] === ";"){
                let index = parseInt(str.slice(i,j))
                res.push(this.map[index])
                j += 1
                i = j
                continue
            }
            j += 1
        }
        return res
    }
}
