"""
https://leetcode.com/problems/next-greater-element-i/
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Brute Force Solution
        For each number in nums1 that corresponds to a value in nums2:
            check if there's any number greater than that value going to the right
            if so, save it in our result array
        
        # res = [-1 for i in range(len(nums1))]
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             k = j
        #             while (k < len(nums2)):
        #                 if nums2[k] > nums2[j]:
        #                     res[i] = nums2[k]
        #                     break
        #                 k += 1
        # return res
        
        More Optimal Solution
        1) Use a hashmap to store the original index of the elements in nums1,
        2) use an O(1) lookup to see if the element exists in nums2
        and then get the original index of the corresponding element in nums1 from our
        hashmap

        O(N*M)

        # res = [-1 for i in range(len(nums1))]

        # counter = dict()
        # for i in range(len(nums1)):
        #     counter[nums1[i]] = i
            
        # for i in range(len(nums2)):
        #     if nums2[i] in counter:
        #         j = i
        #         while (j < len(nums2)):
        #             if nums2[j] > nums2[i]:
        #                 res[counter[nums2[i]]] = nums2[j]
        #                 break
        #             j += 1
        # return res

        Most Optimal Solution:
        Uses a Stack and HashMap
        Taking the first part of the last approach with the hashmap.. 
        1) If the val in nums2 shows up in nums1, add it to a stack
        2) If there's elements in the stack, and the top of the stack is less than the nums2[i],
            we keep popping off the stack, and see if the top of the stack is still less than nums2[i],
            add it to res

        O(N+M) solution

        Neetcode: 
        https://www.youtube.com/watch?v=68a1Dc_qVq4

        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
    

        counter = {4: 0, 1: 1, 2:2}
        stack = []
        res = [-1, -1, -1]

        first iteration
        stack = [1]

        second iteration
        is 3 greater than 1? yes
        so pop off, save res[1] = 3

        res = [-1, 3, -1]

        is 3 in counter? no, don't add to stack
    
        third iteration
        stack = []

        is 4 in counter, yes
        add to stack

        fourth iteration
        stack = [4]

        is 2 greater than 4, no
        is 2 in counter? yes, add to stack

        stack = [4, 2]

        returns res = [-1, 3, -1]

        """

        res = [-1 for i in range(len(nums1))]
        counter = dict()
        for i in range(len(nums1)):
            counter[nums1[i]] = i
        stack = []
        for i in range(len(nums2)):
            if len(stack) > 0:
                while (len(stack) > 0 and stack[-1] < nums2[i]):
                    index =  counter[stack[-1]] 
                    res[index] = nums2[i]
                    stack.pop()

            if nums2[i] in counter: 
                stack.append(nums2[i])
        return res



     