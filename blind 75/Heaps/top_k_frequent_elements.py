'''
https://leetcode.com/problems/top-k-frequent-elements/
'''
from heapq import nlargest, heappop
"""
Revisited on 7/18/2023
for heap problems, remember that you can construct
a heap using a list of tuples, where one of the elements in the tuple
is the comparator, i.e the first element of the tuple is the frequency of the element
and the second is the number

remember that python's default implementation of heapify will result in a min heap,
so you need to inverse the comparator (in this case, setting the frequency to negative) 
so that the most frequent element ends up as the root of the heap

"""

""" a short O(NLogN) solution """
class Solution2:
	def topKFrequent(self, nums: [int], k: int) -> [int]:
		countDict = dict()
        for i in range(len(nums)):
            if nums[i] in countDict:
                countDict[nums[i]] += 1
            else:
                countDict[nums[i]] = 1
        # sort the dict based on values, this creates a list of tuples where
        # the key is first element and the value is the second element
        # this works as an ONLogN solution
        sortedTuples = sorted(countDict.items(), key=lambda x: x[1], reverse=True)
        return [sortedTuples[i][0] for i in range(k)]

class Solution:
    ## O(N^2) solution, O(N) space
    ## at the top level while loop, we may iterate over each number in the worst case
    ## (i.e list with all unique elements) which is O(N)
    ## and then finding the most frequent element is O(N), as well as removing the element
    ## for a total of O(N^2)
    ## can we do better?
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        j = 0
        val = []
        ## find the most frequent element and add to result list
        ## remove it from the list and increment j
        ## repeat this process until j == k, or the length of our nums list becomes zero
        while (j < k and len(nums) > 0):
            most_frequent = self.findMostFrequentElement(nums)
            val.append(most_frequent)
            nums = self.removeMostFrequentElements(most_frequent, nums)
            j+=1
        return val
    def findMostFrequentElement(self, nums):
        counter = dict()
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1
        most_frequent = 0
        cur_max_count = 0
        for num in counter:
            count = counter[num]
            if (count  > cur_max_count):
                cur_max_count = count
                most_frequent = num
        return most_frequent
            
    def removeMostFrequentElements(self, most_frequent, nums):
        n = []
        for num in nums:
            if num != most_frequent:
                n.append(num)
        return n 
    
    ## O(NLogK) 
    ## building the heap is the bottleneck since each insertion is O(NLogK), where LogK is the height of the Heap
    ## and we have N elements to insert into the heap
    ## afterwards, we pop off the heap n amount of times, the pop operation is OLogk, and we repeat N times
    ## thus O(NLogK) overall

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## if K is equal to the length of nums
        ## we don't need to perform any operations
        if (k == len(nums)):
            return nums
        counter = dict()
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1
        heap = []  
        for key in counter:
            ## because want to create a max heap (and the default python implementation is min heap, 
            ## we will invert the comparator, which is the frequency of the element)
            heap.append((-counter[key], key))
        ## heapify is an O(N) operation
        heapq.heapify(heap)
        output = []
        for i in range(k):
            ## heappop is a LogK operation, performed k times
            ## because each heap element is a tuple, we will return tuple[1] to get the element itself
            output.append(heapq.heappop(heap)[1])
        return output

    ## these above steps are combined into one built-in nlargest element in python
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## if K is equal to the length of nums
        ## we don't need to perform any operations
        if (k == len(nums)):
            return nums
        ## get the frequency of each element using dict
        counter = dict()
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1
        
        ## place the elements in a max heap where the most frequent element is the max
        ## the built in heapq library with the nlargest method can take an iterable and automatically return the n largest 
        ## elements based on our frequency, which is used as a key
        return heapq.nlargest(k, counter.keys(), key = lambda c : counter[c])



