class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Merge Sort
        
        Continually split down the middle until the lengths of the arrays are 1
        apply merge two sorted lists
        
        Important:
        When dealing with variable length arrays and slicing, to find the midpoint,
        just do len(nums)//2, and do nums[:mid] for the left, nums[mid:] for the right
        instead of specififying the lengths in the slice operator to avoid off by one errors.

        Time: O(NLogN)
        Space: O(N) (due to the slicing)

        
        """
        def merge(leftHalf, rightHalf):
            len1 = len(leftHalf)
            len2 = len(rightHalf)

            i = 0
            j = 0
            res = []
            while (i < len1 and j < len2):
                if leftHalf[i] < rightHalf[j]:
                    res.append(leftHalf[i])
                    i += 1
                elif leftHalf[i] > rightHalf[j]:
                    res.append(rightHalf[j])
                    j += 1
                else:
                    res.append(leftHalf[i])
                    res.append(rightHalf[j])
                    i += 1
                    j += 1
            if i == len1:
                while (j < len2):
                    res.append(rightHalf[j])
                    j += 1
            elif j == len2:
                while (i < len1):
                    res.append(leftHalf[i])
                    i += 1

            return res

        if len(nums) > 1:
            mid = len(nums)//2
            leftHalf = self.sortArray(nums[:mid])
            rightHalf = self.sortArray(nums[mid:])
            
            res = merge(leftHalf, rightHalf)
            return res
        else:
            return nums
        