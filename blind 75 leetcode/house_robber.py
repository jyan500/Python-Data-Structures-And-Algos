class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        nums = [2,7,9,3,1]
        
        one recursion branch starting with picking 2
        2 is chosen <---> 9 3 1 (7 is not an option because its adjacent to 2)
        9 is chosen <---> 1 (3 is not an option because its adjacent to 9)
        1
        total = 2+9+1=11
        
        backtrack to 9 being chosen.. no other options besides 1!
        backtrack to 2, let's choose 3 this time
        
        3 is chosen <---> no other options because 9 and 1 are both adjacent to 3
        total = 2+3=5
        
        backtrack to 2 being chosen ...
        1 is chosen <---> 9
        9 is chosen <---> (no other options because 3 is adjacent to 9)
        
        total = 11 (same as we got before)
        
        backtrack ...
        
        now choosing 7
        
        7 <---> 3, 1 (we can't choose 2 or 9 because they're both adjacent to 7)
        3 is chosen <---> (no other options because 1 is adjacent to 3)
        
        total = 7+3=10
        
        backtracking ...
        1 is chosen <---> (no other options because 3 is adjacent to 1)
        
        total = 7+1 = 8
        
        '''
        ## function call to first approach
        ## return self.search(nums, 0, 0)

        ## function call to topDown
        return self.topDown(nums, len(nums))
    ## my first approach (brute force by splitting the array down into smaller subproblems until the array is empty)
    def firstApproach(self, nums, total, cur_max):
        if (not nums):
            # print('base case empty list, returning total: ', total)
            return total
        for i in range(len(nums)):
            # print('nums: ', nums)
            ## pick an element
            chosen = nums[i]
            ## recur down the other options that aren't adjacent to the one we just picked
            ## [2,7,9,3,1]
            ## i.e 2 is chosen, get all the other elements besides the index before and after it
            if (i == 0):
                n = nums[i+2:]
            elif (i == len(nums)-1):
                n = nums[:i-1]
            else:
                n = nums[:i-1] + nums[i+2:]
            # print('chosen: ', nums[i])
            # print('total: ', total + chosen)
            # print('cur_max: ', cur_max)
            # print('going into recursive call: max(' + str(cur_max) + ', self.search(' + str(n) + ', ' + str(total) + ' + ' + str(chosen) + ', ' + str(cur_max) + ')')
            cur_max = max(cur_max, self.search(n, total + chosen, cur_max))
            
        # print('end of recursive branch, returning cur_max: ', cur_max) 
        return cur_max

    ## top down approach (without memoization) (traverse the list from right to left starting at len(nums)-1)
    ## O(2^n) time complexity
    ## O(1) space
    def topDown(self, nums, i):
    	if (i <= 0):
    		return 0

    	## option a) pick the current element and recur down the i-2 element (we skip i - 1 since we rob can't that house since its adjacent)
    	current_house = nums[i-1] + self.topDown(nums, i-2)

    	## option b) skip the current element and recur down the i-1 element
    	next_house = self.topDown(nums, i-1)

    	## return the max of what we can make when choosing the current house vs choosing the previous house
    	return max(current_house, next_house)
    ## top down with memoization
    ## O(N) time (we eliminate having to go down repeated subproblems, so essentially we're just visiting each element one time)
    ## O(N) space (for the size of the dictionary)
    def topDownMemoize(self, nums, i, memo):
		## save our current index within this subproblem here
    	key = i
    	## if we've already been to this house, we know the max amount we can make, so just return that amount
	   	if (key in memo):
    		return memo[key]
    	if (i <= 0):
    		memo[i] = 0
    		return 0
    	else:
    		current_house = nums[i-1] + self.topDown(nums, i-2, memo)
    		next_house = self.topDown(nums, i-1, memo)
    		## for the current index, save how much we can make by either going down the current house or the next house
    		memo[key] = max(current_house, next_house)
    		return memo[key]

    ## bottom up solution
    ## 



