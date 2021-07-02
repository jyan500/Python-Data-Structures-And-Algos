class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    def alternativeSolution(self, nums: List[int]) -> bool:
    	counter = dict()
    	for i in nums:
    		if i in counter:
    			return True
    		else:
    			counter[i] = 1
    	return False
            