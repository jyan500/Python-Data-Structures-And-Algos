class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2/25/2025
        """
        O(N) Time
        O(N) space solution using a set
        newArr = []
        noDups = set()
        for i in range(len(nums)):
            if nums[i] not in noDups:
                newArr.append(nums[i])
                noDups.add(nums[i])
        N = len(newArr)
        for i in range(N):
            nums[i] = newArr[i]
        return N
        """
        """
        Two pointers approach:
        1) Keep two pointers starting at 0
        2) Increment the right pointer until the element at the left pointer and element
        at the right pointer are no longer the same.
        3) If so, set the left pointer + 1 element to be the right pointer element, and then
        increment both pointers
        O(N) Time
        O(1) Space

        Example:
        numUniques = 1 (starts out at 1, because there'll always be at least one element in the front)
        1 1 2 3 4 4 4
        l = 0
        r = 0
        l = 0
        r = 1, if s[l] == s[r], this means they are duplicates
        l = 0
        r = 2, s[l] != s[r], so there are no longer duplicates of the element at s[l]
        take s[l+1] and modify it to the value of s[r], then increment l so
        we keep track of the next element
        and the increment the unique element count by 1
        increments numUniques to 2
        
        now nums should be 1 2 2 3 4 4 4
                             ^ ^
                             l r
        l = 1
        r = 2

        increments r to 3
        nums[r] != nums[l] again, so
        set nums[l+1] = 3
        increments numUniques to 3
        now nums should be 1 2 3 3 4 4 4
                               ^ ^
                               l r
        
        increments r to 4
        nums[r] != nums[l] again so,
        set nums[l+1] = 4
        increments numUniques to 4
        now nums is 1 2 3 4 4 4 4
                          ^ ^
                          l r
        finally, we can continue incrementing as the rest are duplicates,
        so in the end, it should return 4              

        Note we only care about the 1 2 3 4, as opposed to the 4_4_4 after, since
        these are treated as "underscores" when being evaluated

        """
        l = 0
        r = 0
        numUniques = 1
        while (r < len(nums)):
            if nums[l] != nums[r]:
                if (l + 1 < len(nums)):
                    nums[l+1] = nums[r]
                r += 1
                l += 1   
                numUniques += 1
            else:
                r += 1
        return numUniques

"""
See remove duplicates from sorted array II
Similar solution, except the elements can only show up once rather than twice.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = dict()
        numUnderscores = 0
        firstUnderscore = 0
        for i in range(len(nums)):
            if nums[i] in counter:
                nums[i] = "_"
                if numUnderscores == 0:
                    firstUnderscore = i
                numUnderscores += 1
            else:
                counter[nums[i]] = 1
        j = firstUnderscore
        for i in range(firstUnderscore, len(nums)):
            if nums[i] != "_":
                nums[j] = nums[i]
                j += 1
        for k in range(j, len(nums)):
            nums[k] = "_"
        
        
        return len(nums) - numUnderscores
        