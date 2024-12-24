class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        """
        Brute Force:
        Out of an array of size N, pick N - 2 elements.
        Sum up these elements and see if it equals to one of the two remaining elements left.
        If so, the other outlier element (not the one that equals the sum) is a potential answer,
        but try to maximize it
        
        Approach:

        One thing to notice is that if you remove the outlier element, you should be left with a given sum
        that includes the number that's **supposed** to add up to the sum of (N-2) elements. If you were to divide
        this number by two, the number that's **supposed** to add up to the sum of (N-2) elements should be present
        
        for example:
        2,3,5,10
        the total sum is 20
        If we remove 10, we get 10
        that is the sum of (2,3,5)
        since in this example, N - 2 is 2, normally we'd pick 2 elements,
        so 2 + 3 = 5. 
        So 10/2 is also 5, meaning that by choosing 10 as the outlier,
        the other remaining number 5 adds up to the sum of the last elements in the array
        that haven't been chosen.
        
        [-2,-1,-3,-6,4]
        if you removed -6 as the outlier,
        4 + -2 + -1 + -3 = -2, -2/2 = -1, in this case
        -1 is the element that sums up to 4 + -3 + -2. However, there is another answer
        we could get, if we continued the iteration
        
        if instead we removed 4 as the outlier,
        -2+-1+-3+-6 = -12
        -12/2 = -6, and -6 exists in our array, therefore,
        the outlier would be 4, which is greater than if we picked -6 as the outlier
        
        Therefore, the approach is
        1) Use a hashmap to map all the elements to their indices, it's possible that multiple elements with the same value exist, so in that case, map it to a set of the possible indices
        2) get the total sum of the array
        3) loop through the nums array and subtract the current element from the total sum to get remaining sum
        check to see if the remaining sum / 2 exists in the hashmap, along with a secondary condition that
        the element found cannot be the same element at the same index that we chose.
        
        for example:
        [6,-31,50,-35,41,37,-42,13]
        
        
        if you were to remove 13 as the outlier, you'd get a remaining sum of 26. dividing by 2 would get
        13. However, 13 is not a valid answer, as this is the same element that we just removed as the outlier,
        but by definition, it has to be a different element since we choose N - 2 elements to sum up, 
        and the remaining numbers have to be the sum of N - 2 AND the outlier.

        (The actual answer here is -35)
        
        4) If the element is found, that means that the current element we removed from the sum is our outlier,
        so we can set it to max() and see if we find a bigger outlier available.
        
        O(N) Time
        O(N) Space
        
        
        """
        from collections import defaultdict
        indexMap = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in indexMap:
                indexMap[nums[i]].add(i)
            else:
                indexMap[nums[i]] = set([i])
        
        total = sum(nums)
        res = float("-inf")
        for i in range(len(nums)):
            remaining = total - nums[i]
            potentialSumNum = remaining / 2
            # if the potential sum number exists and the index of that element is not
            # the one we just chose, since the potential sum number has to be a different element.
            if potentialSumNum in indexMap and (i not in indexMap[potentialSumNum] or len(indexMap[potentialSumNum]) > 1):
                # here, nums[i] is the outlier since we removed it from the total sum,
                # and we were able to find the number
                res = max(res, nums[i])
        return res
            