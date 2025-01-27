class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Neetcode: https://youtu.be/oUnF7o88_Xc
        Adapted solution from here: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solutions/6271057/binary-search-after-finding-the-pivot

        in search in rotated sorted array I, the way 
        to find the "pivot" index was to figure out whether the 
        left most element was greater, to search the left side.
        Otherwise, search the right side.

        However, with duplicates. There's a chance that the 
        current mid point element == right side element 
        or the left side. For example, 
        1 2 2 2 2 2 2 2 3
        pivoted to:
        2 2 2 2 2 3 1 2 2
        in this pivoted version, if the mid was index 2 for example,
        because nums[mid] = 2, and nums[left] = 2, and nums[right] also is 2,
        it's not possible to tell which side to search using binary search.

        """

        def search(l, r, nums, target):
            mid = (l + (r-l)//2)
            # need to search the left side if the cur mid is bigger than
            # the target to find smaller elements

            if nums[mid] == target:
                return True
            if l >= r:
                return False
            # we don't know which half to search, so we just iterate the left
            # similar to linear scan.
            if nums[mid] == nums[l]:
                return search(l+1,r,nums,target)
            if nums[l] <= nums[mid]:
                # if the target is on the left half,
                # search left, otherwise search right
                if nums[l] <= target < nums[mid]:
                    return search(l, mid, nums, target)
                return search(mid+1, r, nums, target)
            else:
                # if the target is on the right half, search right
                # otherwise search left
                if nums[mid] < target <= nums[r]:
                    return search(mid+1, r, nums, target)
                return search(l, mid, nums, target)
        # run the binary search on both sides of the array
        # to account for the duplicates, since the target
        # could be on either side
        return search(0, len(nums)-1, nums, target)