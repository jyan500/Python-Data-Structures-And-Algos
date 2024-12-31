"""
https://www.youtube.com/watch?v=IPunhuBAlI4&ab_channel=AlgorithmsSimplified
Time: O(N)
Space: O(N)

1) The key concepts behind this problem are cumulative sum and binary search
- we can use the cumulative sums to depict the ranges at which a random number between 1 ... sum(weights) 
  can be chosen

  w = [1, 3, 2, 9] sum: 15
index  0  1  2  3

index 0 has a 1/15 chance of being chosen
index 1 has a 3/15 chance of being chosen
index 2 has a 2/15 chance of being chosen
index 3 has a 9/15 chance of being chosen

Using cumulative sums...

cumulative = [1,  4,    6,    15   ]
                (3+1) (2+4) (6+9)

would result in this, where the indexes represent the ranges below

1 | 2 3 4 | 5 6 | 7 8 9 10 11 12 13 14 15

0     1      2               3

1) pick random int r, where r is between 1, sum(w)
2) use binary search on cumulative sums to determine where r resides

i.e if r is 7

left = 0
right = len(cumulative sum) - 1 = 3

mid = 0 + (3 - 0) // 2 = 1

cumulative sum[mid] = 4

7 > 4, therefore we set the left bound to be mid + 1 to search the right half

left = 2
right = 3

mid = 2 + (3-2) // 2 = 2 

cumulative sum[mid] = 6

7 > 6, set the left bound to be mid + 1 to search the right half

left = 3
right = 3

while loop ends

return left, which is correct because 7 falls in the range represented by index 3 (7 to 15)


"""

class Solution:
    def __init__(self, w: List[int]):
        self.total = 0
        self.cumulativeSum = []
        total = 0
        for i in range(len(w)):
            total += w[i]
            self.cumulativeSum.append(total)
        self.total = total

    def pickIndex(self) -> int:
        import random
        rand = random.randint(1, self.total)
        # this can be made more efficient using binary search
        # for index, weight in enumerate(self.cumulativeSum):
        #     if rand <= weight:
        #         return index
        left = 0
        right = len(self.cumulativeSum)-1
        while (left < right):
            mid = left + (right - left) // 2
            if rand == self.cumulativeSum[mid]:
                return mid
            elif rand < self.cumulativeSum[mid]:
                right = mid
            else:
                left = mid + 1
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        """ 
        https://algo.monster/liteproblems/528
        First Approach:
        to bias the weight such that you have a specific probability of picking a certain element,
        duplicate the element by the amount of times indicated by its weight.
        
        For example:
        w = [1, 3]
        the numbers we choose from are the indices of w, so 0 and 1
        since index 0 has a weight 1, we duplicate "0" one time
        since index 1 has a weight of 3, we duplicate "1" three times
        
        self.weights = [0, 1, 1, 1]
        
        by definition, there should be a 75% chance of picking 1, and a 25% chance of picking 0 
        if randomly choosing within self.weights
        
        The issue with this solution is that it's not very memory efficient.
        
        --------------------
        More optimized using Prefix Sum:
        
        Rather than duplicating each number by the same amount of times as its weight,
        you can keep a running total of the amount of times each number should appear (prefix sum)
        
        w = [1, 3]
        self.weights = []
        total = 0
        
        total += w[0] = 1
        self.weights = [1]
        
        total += w[1] = 4
        self.weights = [1, 4]
        
        self.total = 4
        
        Next, when picking the index,
        you can generate a number between 1 and self.total randomly.
        
        then, iterate through self.weights, and check whether the picked number <= self.weights[i],
        if so, this means that this randomly chosen number corresponds to the current index i
        
        for example:
        rand(1, self.total) 
        
        if 2 is chosen
        [1, 4], 
        2 is greater than 1, but less than 4. Therefore, the index chosen would correspond to the index where 4 is (which is 1)
        
        ------------------
        Further optimized with binary search
        
        In pickWeight function, apply binary search to determine the corresponding index of the chosen random number.
        
        Whenever the value at our midpoint > randomly chosen number,
        we search left, since we need a smaller number, because we want to find the point where our midpoint value == randomly chosen number
        Otherwise,
        we search right
        
        if randomly chosen == self.weights[mid], return mid
        however, if the left >= right, return left, because this left will contains the closest index where the randomly chosen number is greater
        
        for example:
        w = [1, 2, 3]
        self.weights = [1, 3, 6]
        
        self.total = 6
        when a random number between 1, self.total is chosen, i.e 4
        when performing binary search,
        since 4 > the midpoint of 3, we search right
        4 < 6, so we search right
        the left index is >= right index now, so we return the left index, which is 2
        
        i.e if 2 is chosen,
        2 < 3, so the index at 3 is chosen 
        
        if 1 is chosen
        1 < 3, so search left
        1 == 1, return midpoint here which is 0
        
        """ 
        self.weights = []
        total = 0
        for i in range(len(w)):
            total += w[i]
            self.weights.append(total)
        self.total = total
        
    def pickIndex(self) -> int:
        import random
        rand = random.randint(1, self.total)
        def binarySearch(left, right):
            mid = left + ((right-left)//2)
            if self.weights[mid] == rand:
                return mid
            if left == right:
                return left
            if self.weights[mid] > rand:
                return binarySearch(left, mid)
            else:
                return binarySearch(mid+1, right)
        return binarySearch(0, len(self.weights)-1)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()