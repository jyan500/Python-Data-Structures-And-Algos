# DS and Algos Cheatsheet
- Writing this as a quick review/knowledge dump right before upcoming technical screens to review common
patterns, hopefully this can help you too.

## Python: 

### Hashmaps
- use can use Counter() if you need char as key and count as value, otherwise just use dict()
    ```
    from collections import Counter
    a = [1,2,2,3]
    c = Counter(a)
    """
    evaluates to 
    c = {1: 1, 2: 2, 3: 1}
    """
    ```
### Prefix/Suffix Sum
- If a cumulative sum is necessary, think about storing the prefix/suffix sums in the array:
    ```
    # prefix
    for i in range(1, len(n)):
        prefix[i] = prefix[i-1] + prefix[i]
    # suffix
    for i in range(len(n)-2,-1,-1):
        suffix[i] = suffix[i+1] + suffix[i]
    ```
### Two Pointers
- two pointers starting from opposite sides of the array and moving inwards towards each other
	stop when `l > r`, such as [three sum](https://leetcode.com/problems/3sum/), [container with most water](https://leetcode.com/problems/container-with-most-water/)
- [longest palindromic subsequences](https://leetcode.com/problems/longest-palindromic-substring/), starts both indices from middle and goes outwards
- [merge two sorted arrays](https://leetcode.com/problems/merge-sorted-array/), you keep one pointer still while moving the other. And once meeting a specific condition,
	move the other pointer

### Sliding Window
- You can avoid repeated work like double for loops by shifting items out of a sliding window, allowing you to solve a problem in one pass. (i.e [find all anagrams in string](https://leetcode.com/problems/find-all-anagrams-in-a-string/))
- You may need to use a hashmap as a way of keeping track whether to remove items from a sliding window based on character count (i.e [min window substring](https://leetcode.com/problems/minimum-window-substring/))

### Intervals
- usually want to sort the list of intervals first
- remember that an interval is considered overlapping if the `previous end > current start`
	```
	prev: ----- 
	cur:     ------
	```
- Review [Insert Interval](https://leetcode.com/problems/insert-interval/), [Merge Interval](https://leetcode.com/problems/merge-intervals/)
### Stacks
- Use a stack if you need to remember a previous result of something (i.e [valid parenthesis](https://leetcode.com/problems/valid-parentheses/))
- always remember to check if the stack is empty or not before accessing the top
- you can push an item, as well as it's index within a tuple on the stack if it's appropriate for the problem. (i.e [min remove to make valid parenthesis](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/))
### Queues
- `from collections import deque`, `q.popleft()`
- BFS
- [Level Order Traversal of a Tree](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- In a simulation type problem (i.e [push dominoes](https://leetcode.com/problems/push-dominoes/)) where the state of
	a given input like an array affects the next state, see if you can push the given state
	onto a queue
### Heaps
- `import heapq`
- You can heapify an array of tuples like so in [k closest points to origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- `[(distance, coords), (distance, coords)]`
- Remember:
- `heapq.heapify(heap)`
- `heapq.heappop(heap)`
### Linked lists
- [reverse linked list](https://leetcode.com/problems/reverse-linked-list/)
    ```
    prev = None
    while (head != None):
    	curr = head
    	head = head.next
    	curr.next = prev
    	prev = curr
    return prev
    ```
- [finding the middle of a linked list](https://leetcode.com/problems/middle-of-the-linked-list/), use fast and slow pointer:
    ```
    """
    If the fast pointer reaches the end of the list, that means it is an even number of nodes.
    If it is none, that means it's odd number. 
    """
    slow = head
    fast = head.next
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    
    """
    make sure to return the "second" middle node, so in the case of even numbered nodes,
    return slow.next, and for odd numbered, return slow
    """
    return slow
    ```
- see if you can use a dummy node, such as `ListNode(0)`
  and then return dummy.next to avoid edge cases where
  you need to modify the head of a linked list

### Binary Search
- Remember if the input array is **sorted**, see if you can use binary search
- Mid point is `left + (right - left)//2` to avoid integer overflow
- Can use recursion or `while (l < r)`
- if value is less than mid, search left by setting the boundaries `left to mid - 1`
- if value is greater than mid, search right by setting the boundaries `mid + 1 to right`

### Trees
- Binary Search Tree
    - If value is less than root, search left
    - If value is greater than root, search right
- Remember that the inorder traversal of a BST is it's sorted array
- [Invert a Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
    `root.left, root.right = root.right, root.left`
- [Max depth of the Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
    `1 + max(height(root.left), height(root.right))`
- [Same Tree](https://leetcode.com/problems/same-tree/)
    ```
    # if both roots don't exist
    if (not p and not q):
        return True
    # if one root is null but the other exists
    if (not p or not q):
        return False
    # if both roots exist and the values are the same
    if (p and q):
        return p.val === q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)
    ```
- Inorder
```
search(root.left)
print(node)
search(root.right)
```
- preorder
```
print(node)
search(root.left)
search(root.right)
```
- postorder
```
search(root.left)
search(root.right)
print(node)
```
### DFS
- recursive
	```
	for n in neighbors:
		if n not in visited:
			visited.add(n)
			dfs(n)
	```

### BFS
-iterative
```
while (queue):
	n = queue.popleft()
	for edge in n:
		if edge not in visited:
			visited.add(edge)
			queue.append(edge)
```
### Graphs
- create an adjacency list first, for example in [course schedule](https://leetcode.com/problems/course-schedule/)
```
    numCourses = 3, prerequisites = [[0,1], [1,2]]
    adjList = dict()
    for i in range(len(numCourses)):
        adjList[i] = []
    for i in range(len(prerequisites)):
        course, prereq = prerequisites[i]
        adjList[course].append(prereq)
    
    """ 
    evaluates to:
    adjList = {
        0: [1],
        1: [2],
        2: []
    }
    
    so 2 does not have any prereqs, but 2 is a prereq of 1
    and 1 is a prereq of course 0
    """
```
### Recursion and Backtracking
- Remember to identify the subproblem and how we can decrease the input space
    for each subproblem
- Draw a decision tree and figure out the result at each branch
- 0, 1 knapsack relation (i.e [house robber](https://leetcode.com/problems/house-robber/)). Do we rob house at `i+1`, or do we skip it and rob house at `i+2` instead? What's the max we can make if we can't rob adjacent houses?
    ```
    # base case
    houses = [...]
    def rob(i):
        if (i >= len(houses)):
            return 0
        # if you rob i by adding houses[i] to the total, you can only i+2 and not i+1
        # since i and i+2 are not adjacent
        robCurrent = houses[i] + rob(i+2)
        robNext = rob(i+1)
        return max(robCurrent, robNext)
    ```
- Memoize using `dict()` and store the result as a value and the key as that particular index to
    avoid going down repeated subpaths. If we already know what the best solution for that subpath is, just recall that in the dict. Usually this cuts time complexities from exponential to O(N) or O(N^2) depending on the problem
    ```
    cache = dict()
    def rob(i):
        if (i in self.memo):
            return self.memo[i]
        if (i >= len(houses)):
            self.memo[i] = 0
            return 0
        robCurrent = houses[i] + rob(i+2)
        robNext = rob(i+1)
        self.memo[i] = max(robCurrent, robNext)
        return self.memo[i]
    ```
- Think about if you may need to loop through a set of constants within the recursion, if that happens, you'll need to store the result outside of the loop (i.e coin change)
- In 2D DP problems such as edit distance, you may need to store a tuple as the key within the `dict()` instead.


