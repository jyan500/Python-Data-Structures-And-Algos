"""
Revisited 1/27/2026 with the optimal solution
Key Concept: 
1) Dictionary where the key is the val nums[i] and the value is the indices
2) When looping through the array, track the index of the last occurrence of nums[i]
3) if nums[i] is seen again, we subtract the value between the current and last occurence
and see if the absolute value is <= k, if so return true. Otherwise update the value
of nums[i] and the index

https://leetcode.com/problems/contains-duplicate-ii/

Time: O(N)
Space: O(N)
"""
class Solution:
    def containsNearbyDuplicateOptimal(self, nums: List[int], k: int) -> bool:
        """
        nums[i] == nums[j], values are equal
        abs(i - j) <= k, the absolute difference between their indices is less than or equal to k
        """
        indexMap = dict()
        for i in range(len(nums)):
            if nums[i] in indexMap:
                if abs(i - indexMap[nums[i]]) <= k:
                    return True
            # if the distance between the two indices is too large, 
            # OR we haven't seen this number in the array yet
            # update the index for this value to the current index
            # so if we find another occurrence in the array, the distance should be shorter.
            indexMap[nums[i]] = i
        return False 
    

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Brute Force Method
        nums[i] == nums[j], values are equal
        abs(i - j) <= k, the absolute difference between their indices is less than or equal to k
        """
        indexMap = dict()
        for i in range(len(nums)):
            if nums[i] in indexMap:
                indexMap[nums[i]].append(i)
            else:
                indexMap[nums[i]] = [i]
        for key in indexMap:
            for i in range(1, len(indexMap[key])):
                if abs(indexMap[key][i] - indexMap[key][i-1]) <= k:
                    return True
        return False
    