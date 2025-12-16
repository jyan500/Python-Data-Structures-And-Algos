/* 
	https://algo.monster/liteproblems/2633
	(This is a premium problem on leetcode)	

	This problem asks you to implement a function that converts JavaScript values into their JSON string representation 
	without using the built-in JSON.stringify method.

	The function should handle the following data types:

	null: Should return the string "null"
	string: Should be wrapped in double quotes, e.g., "hello" becomes "\"hello\""
	number: Should be converted to its string representation, e.g., 42 becomes "42"
	boolean: Should return "true" or "false"
	array: Should return elements wrapped in square brackets separated by commas, e.g., [1, 2, 3] becomes "[1,2,3]"
	object: Should return key-value pairs wrapped in curly braces, with keys as strings and separated by commas, e.g., {a: 1, b: 2} becomes "{"a":1,"b":2}"
	Key requirements:

	The output string should not contain extra spaces
	For objects, the order of keys in the output should match the order returned by Object.keys()
	The function should recursively handle nested structures (arrays within objects, objects within arrays, etc.)
*/

const convert = (obj) => {
	if (obj === null){
		return "null"
	}
	else if (typeof obj === "number" || typeof obj === "boolean"){
		return `"${obj.toString()}"`
	}
	else if (typeof obj === "string"){
		return `"${obj}"`
	}
	else if (Array.isArray(obj)){
		// pass this function recursively into map, which will put all the elements
		// into the array and then join them by comma
		return `[${obj.map(convert).join(",")}]`
	}
	else {
		// obj.entries -> gets an array of key, value pairs
		// apply the recursion on the key (just to handle the primitive key),
		// and also on the values themselves, returning "":"" pairs, and then
		// joining them together by comma
		return `{${Object.entries(obj).map(([key, value]) => {
			return `${convert(key)}:${convert(value)}`
		}).join(",")}}`
	}
}

convert({"a": {"d": [false, null, "b", 2]}, "b": [2,3,{"c": null}]})
/* '{"a":{"d":["false",null,"b","2"]},"b":["2","3",{"c":null}]}' */
