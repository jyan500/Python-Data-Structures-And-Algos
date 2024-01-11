"""
This is a modified version of 3-sum, where the result
cannot contain any duplicate triplets

key concepts: 
sorting the input array
two pointers to avoid an additional loop
see these two vids for reference:
Three Sum: https://www.youtube.com/watch?v=jzZsG8n2R9A&ab_channel=NeetCode
Two Sum II: https://www.youtube.com/watch?v=cQ1Oz4ckceM&ab_channel=NeetCode
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        sortedNums = sorted(nums)
        for i in range(len(sortedNums)):
            # if the previous number is the same as the current,
            # we can ignore it to avoid creating duplicate triplets
            if i == 0 or sortedNums[i] != sortedNums[i-1]:
                left = i+1
                right = len(sortedNums)-1
                while (left < right):
                    # if our total sum is greater than zero, we need to decrease the pointer on the right
                    if sortedNums[i] + sortedNums[left] + sortedNums[right] > 0:
                        right -= 1
                    # if our total sum is less than zero, we need to increase the pointer on the left
                    elif sortedNums[i] + sortedNums[left] + sortedNums[right] < 0:
                        left += 1
                    else:
                        triples.append((sortedNums[i], sortedNums[left], sortedNums[right]))          
                        left += 1
                        # to avoid re-using the same number like in the example below, we need to increment
                        # left until the previous number is no longer equal to the current
                        # -2, -2, 0, 0, 2, 2
                        # after finding the triplet -2, 0, 2 , we need to increment left again since it'd be pointing
                        # at index 3 here (which is 0), which would result in finding the triplet -2, 0, -2 again, so we need
                        # to increment to index 4 (which is 2)
                        while (sortedNums[left] == sortedNums[left-1] and left < right):
                            left += 1
        return triples
