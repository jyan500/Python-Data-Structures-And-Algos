class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        solution with built in sort,
        looking at all indices where the results are different than the sorted version
        """
        # sortedHeights = sorted(heights)
        # res = 0
        # for i in range(len(heights)):
        #     if heights[i] != sortedHeights[i]:
        #         res += 1
        # return res
        """
        Merge sort version
        """
        def merge(array1, array2):
            res = []
            l = 0
            r = 0
            while (l < len(array1) and r < len(array2)):
                if array1[l] < array2[r]:
                    res.append(array1[l])
                    l += 1
                else:
                    res.append(array2[r])
                    r += 1
            if l < len(array1):
                for i in range(l, len(array1)):
                    res.append(array1[i])
            elif r < len(array2):
                for i in range(r, len(array2)):
                    res.append(array2[i])
            return res
        def mergeSort(array):
            # arrays with length greater than 1 can be split further
            if len(array) > 1:
                mid = len(array)//2
                left = mergeSort(array[:mid])
                right = mergeSort(array[mid:])
                return merge(left, right)
            return array
        
        sortedHeights = mergeSort(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                res += 1
        return res
                