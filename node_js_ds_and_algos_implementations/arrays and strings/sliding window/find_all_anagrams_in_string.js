/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    // Function to compare two maps
    function mapsEqual(map1, map2) {
        if (map1.size !== map2.size) return false;
        for (let [key, value] of map1) {
            if (map2.get(key) !== value) return false;
        }
        return true;

    }
    /* 
    https://youtu.be/G8xtZy0fDKg 
    Write function to compare two javascript map objects (map objects allow for .size() which is more convenient that regular object)

    Approach:
   	Keep javascript map objects that represent the counts of string p (shorter string) and string s (longer string)
   		- the map s initially tracks the first window from index 0 to p.length - 1
   	If map S === map P initially, that means one anagram was found starting at index 0

   	iterate and perform sliding window starting at p.length to s.length, where l = 0, r = p.length (this is one character
   	after the initial window)
   		add s[r] to the map S
   		decrement s[l] from map S to show that we're shrinking the window size
   		if s[l] not in map S any more, make sure to delete the key

   		increment l
   		if map S === map P, push to index l to the result

	the idea here is that each time we slide the window, we remove the character at l and add the character at r,
	and then update the frequencies. If the maps equal to each other, then the frequencies of all characters
	must be matching, so this is an anagram.

	Time Complexity:
	O(N * 26), the "26" portion comes from the fact that we compare two maps that consist only of 26 alphabetic characters.

	Space:
	O(N)
    */
    let result = [];
    if (p.length > s.length) {
        return result;
    }
    // create frequency maps
    const pCount = new Map();
    const sCount = new Map();

    // creating a map for p string to compare 
    for (let char of p) {
        pCount.set(char, (pCount.get(char) || 0) + 1)
    }
    //first window of string 
    for (let i = 0; i < p.length; i++) {
        let char = s[i];
        sCount.set(char, (sCount.get(char) || 0) + 1)
    }

    // check the first window
    if (mapsEqual(sCount, pCount)) {
        result.push(0)
    }
    //sliding the window
    let l = 0
    for (let r = p.length; r < s.length; r++) {
        // Add new character to window 
        sCount.set(s[r], (sCount.get(s[r]) || 0) + 1)
        sCount.set(s[l], sCount.get(s[l]) - 1)
        if (sCount.get(s[l]) === 0){
            sCount.delete(s[l])
        }
        ++l
        if (mapsEqual(sCount, pCount)) {
            result.push(l);
        }
    }

    return result;

};