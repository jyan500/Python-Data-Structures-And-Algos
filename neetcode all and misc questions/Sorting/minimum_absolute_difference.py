class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        Approach:
        1) sort the array
        2) find the minimum absolute difference between the elements in arr
        by comparing the cur element with the previous
        3) find all pairs that have this difference by comparing
        the cur with the prev element (this works because it's in sorted order,
        so we know the elements will be as close in distance as possible)
        example 1: [1, 35, 36]
        35 - 1, difference of 34
        36 - 35, difference of 1
        min absolute diffrence here is 1
        example 2: [3,8,-10,23,19,-4,-14,27]
        sorted = [-14, -10, -4, 3, 8, 19, 23, 27]

        You can see that the min absolute difference is 4, and that the pairs
        can be found by comparing the cur with the previous

        Time: O(NLogN)
        Space: O(1) (no additional memory used besides the result array)

        """
        arr.sort()
        minDifference = float("inf")
        for i in range(1, len(arr)):
            minDifference = min(minDifference, abs(arr[i]-arr[i-1]))
        pairs = []
        for i in range(1, len(arr)):
            if abs(arr[i]-arr[i-1]) == minDifference:
                pairs.append([arr[i-1], arr[i]])
        return pairs