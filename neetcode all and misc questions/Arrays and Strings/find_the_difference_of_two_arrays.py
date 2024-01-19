"""
https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        from collections import Counter
        m = set(nums1)
        n = set(nums2)
        res1 = set([nums1[i] for i in range(len(nums1)) if nums1[i] not in n])
        res2 = set([nums2[i] for i in range(len(nums2)) if nums2[i] not in m])
        return [res1, res2]
            