## Stack Data Structure and Some Algorithms that can be solved using Stack
class Stack:
	def __init__(self):
		self.stack = []

	def pop(self):
		return self.stack.pop()

	def push(self, element):
		self.stack.append(element)

	def isEmpty(self):
		return len(self.stack) == 0

	def get_stack(self):
		return self.stack

	def peek(self):
		if (self.isEmpty()):
			return ''
		else:
			return self.stack[-1]

	def __str__(self):
		return '[' + ', '.join(self.stack) + ']'

## Is Balanced Parenthesis Problem 

def isBalancedParenthesis(string):
	s = Stack()
	for i in range(len(string)):
		if (not s.isEmpty()):
			## get the top item of the stack
			top = s.peek()
			## if the top of the stack is an opening brace, and the current char is a closing brace ...
			if isMatch(string[i], top):
				## pop the opening brace off the stack
				s.pop()
				## continue to the next iteration since we don't need to push the closing brace onto the stack
				continue
		s.push(string[i])
	return s.isEmpty()

def isMatch(string1, string2):
	return (string1 == ')' and string2 == '(') or (string1 == ']' and string2 == '[') or (string1 == '{' and string2 == '}')

## Test Cases for Is Balanced Parenthesis Function
test = "(([]))"
test2 = "((["
print(isBalancedParenthesis(test))
print(isBalancedParenthesis(test2))

## Integer to Binary
## Description: Use a stack data structure to convert integer values to binary
## Example: 242
## 242/2 = 121 (242 % 2 = 0)
## 121/2 = 60 (121 % 2 = 1)
## 60/2 = 30 (60 % 2 = 0)
## 30/2 = 15 (30 % 2 = 0)
## 15/2 = 7 (15 % 2 = 1)
## 7/2 = 3 (7 % 2 = 1)
## 3/2 = 1 (3 % 2 = 1)
## 1/2 = 0 (1 % 2 = 1)
## Binary Representation = 11110010

def divideBy2(num):
	stack = Stack()
	while num > 0:
		remainder = num % 2
		stack.push(remainder)
		## floor division
		num = num // 2
	bin_num = ''
	for i in range(len(stack.get_stack())):
		bin_num += str(stack.pop())
	return bin_num

print(divideBy2(242))









