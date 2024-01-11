'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
https://leetcode.com/problems/product-of-array-except-self/
https://www.youtube.com/watch?v=tSRFtR3pv74&t=148s&ab_channel=NickWhiteNickWhite
'''
class Solution:

	# revisited in 2023 using https://www.youtube.com/watch?v=10NJzNaSsrg&ab_channel=ThatIndianCoder
	def alternativeSolution(self, nums: List[int]) -> List[int]:
        # two pass solution
		length = len(nums)
        left = [1 for i in range(length)]
        right = [1 for i in range(length)]
        answer = [1 for i in range(length)]
        # iterate left to right, and calculate the products of every element before i (i-1),
        # ignore index 0 since there's no element to the left
        for i in range(1, length):
            left[i] = nums[i-1] * left[i-1]
        # iterate right to left, and calculate the products of every element after i (i+1)
        # ignore index len(nums)-1 since there's no element to the right
        for i in range(length-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        # to get the product of all elements besides i, multiply the elements of left and right
        for i in range(length):
            answer[i] = left[i] * right[i]
        return answer

    ## I revisited this problem on 8/5/2021, using nick white's solution again
    ## Its O(N) Time and O(N) space
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ## Time complexity = O(N^2)
        ## Space complexity = O(1), no additional space
        ## can we do better?
        # l = []
        # for i in range(len(nums)):
        #     if (i == 0):
        #         l.append(self.multiply(nums[1:]))
        #     elif (i == len(nums)-1):
        #         l.append(self.multiply(nums[:len(nums)-1]))
        #     else:
        #         l.append(self.multiply(nums[:i]+nums[i+1:]))
        # return l
        
        ## https://www.youtube.com/watch?v=khTiTSZ5QZY&ab_channel=NickWhite
        ## the key realization here is that at any given number i, the product we want
        ## is the product of all the numbers to the left * the product of all numbers to the right
        ## so our approach is that for each number, we want a list of all the products to the left of each number
        ## and we also want a list of all the products to the right of each number
        ## the final result would just be the two products multiplied together
        ## we're not going to be able to do this all in one loop so we need multiple loops
        ## to find the left and right products
        
        ## for example, for [1,2,3,4]
        ## for the first element, the product of all the numbers to the left of 1 would just be 1, since there's no numbers to the left of 1
        ## the product of all the numbers to the right of 1 would be 24
        ## so 1 * 24 = 24
        ## for the second element, the product of all the numbers to the left is 1
        ## the product of all the numbers to the right is 12
        ## so the answer is 1 * 12 = 12
        ## for the third element, the product of all the numbers to the left is 2
        ## and the product of all the numbers to the right is 4, so the answer is 2 * 4 = 8
        ## for the fourth element, the product of all the numbers to the left is 1*2*3 = 6
        ## and the product of all the numbers to the right is 1, since there's no numbers to the right
        ## the total answer is 6
        ## final result is 24,12,8,6 which is correct

        N = len(nums)
        left_product = [1] * N
        right_product = [1] * N
        result = [1] * N
        ## calculate the product of all numbers to the left at each index
        for i in range(N):
            if (i == 0):
                ## there's no numbers to the left here since its the first element, so the left product is just 1
                left_product[i] = 1
            else:
                ## the products on the left would simply be multiplying the previous number (nums[i-1]),
                ## with the cumulative product that we've calculated so far (left_product[i-1])
                left_product[i] = nums[i-1] * left_product[i-1]
        ## calculate the product of all numbers to the right at each index, we need to iterate through
        ## the list in reverse to do this
        for i in range(N-1,-1,-1):
            if (i == N-1):
                ## there's no numbers to the right here since its the last element, so the right product
                ## is just 1
                right_product[i] = 1
            else:
                ## the products on the right would simply be multiplying the previous number (from reverse persective, this is actually nums[i+1]) 
                ## with the cumulative product that we've calculated so far (right_product[i+1])
                right_product[i] = nums[i+1] * right_product[i+1]
        
        ## the result at a given index is just all the products of each number to the left * all products of each number to the right
        for i in range(N):
            result[i] = left_product[i] * right_product[i]
        
        return result

    
    def multiply(self, L):
        ans = 1
        for i in range(len(L)):
            ans *= L[i]
        return ans

	def mostEfficientSolution(self, nums: List[int]) -> List[int]:
		## O(1) space
		output = [1]
		## store the prefix values within the output array instead of having a separate prefix array
		for i in range(1, len(nums)):
			output.append(nums[i-1] * output[i-1])
		res = 1
		## calculate the postfix values (stored in res) where we multiply the prefix value by the postfix value,
		## except we multiply by the value of res
		## the value of res is simply the previous value of res times the current index of nums, because
		## that would be the value of every element to the right of that current index 
		for i in range(len(nums) - 1, -1, -1):
			output[i] = output[i] * res
			res = res * nums[i]
		return output

    def productExceptSelf(self, nums: List[int]) -> List[int]:
    	## first Nick White solution with O(N) space
        output = []
        ## get list of products that are after i by looping backwards
        postfix = []
        for i in range(len(nums)):
            postfix.append(1)
        ## note that in the last index of postfix ,the value is 1 since the product of everything to the right of the last item is the number itself
        for i in range(len(nums)-2, -1, -1):
        	## nums[i+1] would be the previous number (in the perspective of looping backwards) times the previous product that we have so far
            postfix[i] = nums[i+1] * postfix[i+1]
        

        ## get list of products that are before i by looping forwards
        prefix = [1]
        ## note that the first index of prefix, the value is 1 since the product of everything to the left of the first item is the number itself
        for i in range(1, len(nums)):
        	## nums[i+1] would be the previous number times the previous product that we have so far
        	prefix.append(nums[i-1] * prefix[i-1])

        ## use the prefix and postfix lists to calculate the product of everything before i and everything after i
        for i in range(len(nums)):
        	output.append(prefix[i] * postfix[i])
        return output

    def firstSolution(self, nums: List[int]) -> List[int]:
    	## first Neetcode Solution with O(N) space
        output = []
        ## get list of products that are after i by looping forwards
        postfix = []
        for i in range(len(nums)):
            postfix.append(0)
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            if (i == len(nums)-1):
                prev = nums[i]
            else:
                prev *= nums[i]
            postfix[i] = prev
        

        ## get list of products that are before i by looping backwards
        prefix = []
        prev = 1
        for i in range(len(nums)):
            if (i == 0):
                prev = nums[i]
            else:
                prev *= nums[i]
            prefix.append(prev)


        ## use the prefix and postfix lists to calculate the product of everything before i and everything after i
        for i in range(len(nums)):
            if (i == 0):
                output.append(postfix[i+1] * 1)
            elif (i >= len(nums)-1):
                output.append(prefix[i-1] * 1)
            else:
                output.append(prefix[i-1] * postfix[i+1])
        return output

