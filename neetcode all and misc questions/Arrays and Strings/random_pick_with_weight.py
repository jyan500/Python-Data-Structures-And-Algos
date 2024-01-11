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