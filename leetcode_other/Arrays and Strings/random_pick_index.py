'''
https://leetcode.com/problems/random-pick-index/
'''
import random
class Solution:
    ## two solutions
    ## first one is to simply store the array nums at first
    ## and then during the pick method, use O(N) time to scan through and add
    ## the indices of the element that equals target, and pick the random index from that array
    ## tradeoff is that we're spending O(N) time and O(N) space per pick operation
    
    ## the other approach (which is implemented) is to keep a hashmap of all the elements and the indices at which they occur
    ## this uses an O(N) time upfront and O(N) space to store this map, but saves time on each pick
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.map = dict()
        for i in range(len(nums)):
            if (nums[i] in self.map):
                self.map[nums[i]].append(i)
            else:
                self.map[nums[i]] = [i]
        

    def pick(self, target: int) -> int:
        
        return self.map[target][random.randint(0, len(self.map[target])-1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)