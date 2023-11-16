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



     