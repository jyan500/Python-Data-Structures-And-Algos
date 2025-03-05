class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Split by spaces,
        what would happen if the string had multiple spaces between each word?
        you would get empty strings in the output after splitting, in this case,
        we should remove these by filtering...

        Reverse the array, and then join the array together with one space as a delimiter

        Time: O(N)
        Space: O(N)
        """
        l = s.split(" ")
        filtered = list(filter(lambda x: x != "", l))
        # reversing an array without iteration involves
        # using the first step of merge sort, which is the splitting 
        # of each array in half, until the array is length 1, and then
        # instead of performing the merge 2 sorted arrays operation,
        # just add the right half to the left half 
        def reverseArray(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr)//2
            leftHalf = reverseArray(arr[:mid])
            rightHalf = reverseArray(arr[mid: ])
            return rightHalf + leftHalf
        reversedArray = reverseArray(filtered)
        return " ".join(reversedArray)
        