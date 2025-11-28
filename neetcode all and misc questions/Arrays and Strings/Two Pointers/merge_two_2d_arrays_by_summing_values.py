class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        find the intersection to get id values that exist in both arrays
        perform similarly to merge 2 sorted arrays, except
        if the id exists in both, 
        merge the values together in the sorted array
        """
        nums1Set = set(num[0] for num in nums1)
        nums2Set = set(num[0] for num in nums2)
        idSet = nums1Set.intersection(nums2Set)
        l = 0
        r = 0
        res = []
        while (l < len(nums1) and r < len(nums2)):
            id1, val1 = nums1[l]
            id2, val2 = nums2[r]
            if id1 in idSet and id2 in idSet:
                res.append([id1, val1+val2])
                l += 1
                r += 1
            elif id1 < id2:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        if l < len(nums1):
            for k in range(l, len(nums1)):
                res.append(nums1[k])
        if r < len(nums2):
            for k in range(r, len(nums2)):
                res.append(nums2[k])
        return res