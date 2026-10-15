"""
	https://algo.monster/liteproblems/2633
	(This is a premium problem on leetcode)	

	This problem asks you to implement a function that converts python values into their JSON string representation 
	without using the built-in json dumps method.

	The function should handle the following data types:

	none: Should return the string "null"
	string: Should be wrapped in double quotes, e.g., "hello" becomes "\"hello\""
	number: Should be converted to its string representation, e.g., 42 becomes "42"
	boolean: Should return "true" or "false"
	array: Should return elements wrapped in square brackets separated by commas, e.g., [1, 2, 3] becomes "[1,2,3]"
	object: Should return key-value pairs wrapped in curly braces, with keys as strings and separated by commas, e.g., {a: 1, b: 2} becomes "{"a":1,"b":2}"
	Key requirements:

	The output string should not contain extra spaces
	For objects, the order of keys in the output should match the order returned by Object.keys()
	The function should recursively handle nested structures (arrays within objects, objects within arrays, etc.)
"""
def stringify(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, bool):
    	return "true" if value else "false"
    if isinstance(value, (int, float)):
        return f"{str(value)}"
    if isinstance(value, (tuple, list)):
        res = []
        for val in value:
            res.append(stringify(val))
        return "[" + ','.join(res) + "]"
    if isinstance(value, dict):
        res = []
        for key in value:
            res.append(f"{stringify(key)}:{stringify(value[key])}")
        return "{" + ','.join(res) + "}"
    raise TypeError(f"Cannot serialize {type(value).__name__}")

if __name__ == "__main__":
	assert stringify(None) == "null" 
	assert stringify("Test") == '"Test"'
	assert stringify(8) == "8"
	assert stringify(True) == "true"
	assert stringify(["a", 8, ["a", 8]]) == '["a",8,["a",8]]'
	assert stringify({True: "b", "a": {"d": ["a", True, 8]}}) == '{true:"b","a":{"d":["a",true,8]}}'
