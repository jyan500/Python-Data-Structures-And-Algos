class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        2 7 11 15
        Because the input array is already sorted,
        we can assume a greedy solution, where
        we set the left pointer to be the 1st number,
        which is also the smallest number
        and then set the right pointer to be the last
        number, which is the biggest number. By summing
        these two numbers initially, if we don't get the right solution,
        we can adjust the pointer values to increase or decrease
        the sum.

        if we add the values the two pointers and check if:
        sum > target, then shift right pointer, since we need
        a smaller number
        sum < target, then shift left pointer,
        since we need a larger number
        sum == target:
            we've found the indices, return the 
            left pointer + 1 , right pointer + 1
            since its 1 indexed

        O(N) Time
        O(1) Space
        """
        l = 0
        r = len(numbers) - 1
        while (l <= r):
            result = numbers[l] + numbers[r]
            if result > target:
                r -= 1
            elif result < target:
                l += 1
            else:
                return [l+1,r+1]
        # there's guaranteed to be exactly
        # one solution, so we can just return here
