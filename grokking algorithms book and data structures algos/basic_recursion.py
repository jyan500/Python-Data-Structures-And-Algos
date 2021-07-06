import math
def sum(l):
	if (len(l) == 0):
		return 0
	if (len(l) == 1):
		return l[0]
	return l[0] + sum(l[1:])

print(sum([2,4,6,8])) ## 20
print(sum([1,2,3,4]))

def list_length(l):
	if (not l):
		return 0 
	return 1 + list_length(l[1:])

print(list_length([2,4,6,8])) ## 4
print(list_length([4,6,8,10,12])) ## 5

def iterative_binary_search(l, num):
	left = 0
	right = len(l) - 1
	while (left <= right):
		mid = (left + right) // 2
		guess = l[mid]
		if (guess == num):
			return mid
		if (guess > num):
			right = mid - 1
		else:
			left = mid + 1
	return None

## returns true if the number is within the sorted list, returns false if not
def recursive_binary_search(l, num):
	print(l)
	if (len(l) == 0):
		return False
	else:
		mid = len(l) // 2
		guess = l[mid]
		if (guess == num):
			return True 
		if (guess > num):
			return recursive_binary_search(l[:mid], num)
		if (guess < num):
			return recursive_binary_search(l[mid+1:], num)

print(recursive_binary_search([2,4,6,8,10,12], 10))
print(recursive_binary_search([2,4,6,8,10,12], 12))
print(recursive_binary_search([2,4,6,8,10,12], 7))
print(recursive_binary_search([2,4,6,8,10,12], 13))
print(recursive_binary_search([2,4,6,8,10,12], 0))
print(recursive_binary_search([2], 4))
print(recursive_binary_search([2,4], 4))

def quick_sort(l):
	if (len(l) < 2):
		return l
	else:
		pivot = l[0]
		after_pivot = l[1:] 
		less = []
		greater = []
		for i in range(len(after_pivot)):
			if after_pivot[i] <= pivot:
				less.append(after_pivot[i])
			if after_pivot[i] > pivot:
				greater.append(after_pivot[i])
		return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 1, 5, 3, 2, 13, 4]))




