/**
 * @param {string} s
 * @return {number}
 */
var maxLengthBetweenEqualCharacters = function(s) {
    /*
    Time: O(N)  
    Space: O(N)
    after some reading, the question is actually just asking
    the biggest distance between two characters
    of the same value
    
    you can use a hashmap to record the indices of all characters, and then find the longest interval

    An important takeaway is figuring out what the problem is actually asking, in this case, it's the length of the substring,
    which is really just the distance between two characters, and NOT the actual substring itself. So you save
    a lot time and memory when you don't need to keep track of that.

    */
    let counter = {}
    for (let i = 0; i < s.length; ++i){
        if (s[i] in counter){
            counter[s[i]].push(i)
        }
        else {
            counter[s[i]] = [i]
        }
    }
    // start at -1, if each character in the string appears only once,
    // then this value will not be changed, which is the proper return
    // for an invalid case
    let maxDistance = -1
    for (let key in counter){
        // if there's instances where two characters are equal to each other
        if (counter[key].length > 1){
            // take the max and min, which should be the last and first index, and subtract
            // to find the distance. 
            // you don't include the two equal valued
            // characters themselves though, so you need to subtract one 
            maxDistance = Math.max(counter[key][counter[key].length - 1] - counter[key][0] - 1, maxDistance)
        }
    }
    return maxDistance
};