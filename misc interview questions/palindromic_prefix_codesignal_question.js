/**
You are given a string s. Consider the following algorithm applied to this string:

Take all the prefixes of the string, and choose the longest palindrome between them.
If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. 
Otherwise, end the algorithm with the current string s as a result.
Your task is to implement the above algorithm and return its result when applied to string s.

Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

Example

For s = "aaacodedoc", the output should be solution(s) = "".

The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". 
The longest one between them is "aaa", so we cut it from s.
Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut it from the current string and obtain the empty string.
Finally the algorithm ends on the empty string, so the answer is "".
For s = "codesignal", the output should be solution(s) = "codesignal".
The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

For s = "", the output should be solution(s) = "".

**/
function solution(s) {
	/** 
		My approach:
		1) find all palindromic substrings that were length 2 or greater, and store their ranges and lengths in array
		2) at each index, find the longest palindrome that started at this index. You'd need to sort the array by length.
		3) make a copy of the string and set the ranges that need to be removed to be empty strings,
			- note that you can only remove ranges where the current range begins immediately after the previous range,
			with no space in between.
		4) return the string
	**/

    let ranges = []
    // find all palindromic subsequences
    for (let i = 0; i < s.length; ++i){
        let j = i
        let left = j 
        let right = j 
        let counter = 1
        while (left >= 0 && right < s.length){
            // note the problem states that the palindrome must be at least 2 characters in length
            if (s[left] === s[right]){
                if (counter >= 2){
                    ranges.push({length: counter, left: left, right: right})
                }
                --left
                ++right 
                counter += 2
            } else {
                break
            }
        }
        left = j 
        right = j + 1
        counter = 2
        while (left >= 0 && right < s.length){
            if (s[left] === s[right]){
                if (counter >= 2){
                    ranges.push({length: counter, left: left, right: right})
                }
                --left
                ++right
                counter += 1
            } else {
                break
            }
        }
    }
    let i = 0
    let maxLengths = []
    // find the longest palindromes that begin at each index
    while ( i < s.length){
        let r = ranges.filter((obj) => obj.left === i)
        if (r.length){
            let sortedRange = r.sort((obj => obj.length))
            maxLengths.push(sortedRange[sortedRange.length-1])
        }
        ++i
    }
    // iterate through max lengths, keep a pointer to track where we're at in the string
    // you need to start removing the range from the string, and then take the "right" attribute and set the pointer to the right
    // attribute of the range that was just removed from the string
    let k = 0
    let prevLeft = 0
    let prevRight = 0
    let removedSections = []
    while (k < maxLengths.length){
        if (prevRight !== 0){
            // if the ranges overlap, then we need to ignore this one since we've already removed
            // a segment of longer length
            if (maxLengths[k].left <= prevRight){
                ++k
                continue
            }
        }
        removedSections.push(maxLengths[k])
        prevLeft = maxLengths[k].left
        prevRight = maxLengths[k].right
        ++k
    }
    let copy = s.split("")
    let pointer = 0
    for (let j = 0; j < removedSections.length; ++j){
    	// you can only remove prefixes, so as soon as one range ends, 
    	// the next range that needs to be removed must be immediately after the previous range,
    	// hence the pointer that keeps track of the previous right.
    	// i.e current left == the previous right
        if (removedSections[j].left == pointer) {      
            for (let h = removedSections[j].left; h <= removedSections[j].right; ++h){
                copy[h] = ""
            }
        }
        pointer = removedSections[j].right + 1
    }
    return copy.join("")

    /**
    Working solution by: 
    https://leetcode.com/discuss/interview-question/801274/Robinhood-coding-question-2/1644021
    User geniusmonir
    **/
	// if (!s) return '';
	// const sLen = s.length;
	// let finalRes = '';

	// let targetStr = s;
	// for (i = 0; i < sLen; i++) {
	// 	let maxPrefixLen = 0;
	// 	// starting at the index 1, find the longest palindrome and set the length of the prefix
	// 	for (let j = 1; j <= targetStr.length; j++) {
	// 		let str = targetStr.substring(0, j);
	// 		let strR = [...str].reverse().join('');
	// 		if (str == strR) {
	// 			maxPrefixLen = j;
	// 		}
	// 	}
	// 	const prefix = targetStr.substring(0, maxPrefixLen);
	// 	const prefixLen = prefix.length;

	// 	if (prefixLen === 1) {
	// 		finalRes = targetStr;
	// 		break;
	// 	}

	// 	if (prefixLen === 0) {
	// 		finalRes = '';
	// 		break;
	// 	}
	// 	targetStr = targetStr.replace(prefix, '');
	// }
 //    return finalRes;
}
