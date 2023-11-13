"""
Key Concepts:
Binary Search and Gauss Summation (n(n+1)/2)
1) Because each ith row contains i coins, we can do a binary search,
where at each mid point, we calculate the amount of coins that it'd take to fill up all
the rows from 1 to mid
so total num of coins that fills all previous rows = mid(mid+1)/2 

Binary search, set up with left = 1, right = n (our total amount of coins, note that this can never be the answer because
(n(n+1)/2), this is going always be greater than n). 

1) if the total num of coins is greater than our n, we've used too many coins, so we need to search the left half
2) if the total num of coins is equal to OR less than our n, that means we could potentially fill more rows, so we search
the right half

Once left >= right and our search ends, this would give us the threshold where we're about to use up all of our coins.
(The closest value to our answer)
we do a final check to see if the total sum at our left pointer > n

if so, we've overshot, so we return left - 1 which would give us all the rows that can be completed using n coins
otherwise, we return left, which would be just the right amount of coins

Time Complexity: Gauss Summmation is O(1), but Binary Search is O(LogN), so O(1) * O(LogN) = O(LogN)

"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        *
        * *
        * * X
        n = 5 coins, each row has i coins

        *
        * *
        * * *
        * * X X

        n = 8 coins, 
        row 1 = 1 coin
        row 2 = 2 coins
        row 3 = 3 coins (total 6) 
        row 4 = 2 coins (total 8 == 8, reached)

        the last row we could fully make was row 3 with 3 coins, output 3

        lower bound = 1
        upper bound = n

        if we're at mid, we know that we used up the sum of 1 ... mid amount of coins
        already

        total = (mid)(mid + 1)/2

        if total <= n:
            we might still be able to fit more coins, search the right half
        if total < n:
            too many coins, search the left half
        """
        left = 1 
        right = n
        def totalSum(n):
            return (n * (n+1))/2
        def search(left, right, n):
            mid = left + (right - left)//2
            # same as total sum formula n(n+1)/2
            total = totalSum(mid)    
            if left >= right:
                return left - 1 if totalSum(left) > n else left
            # we might still be able to fit more coins, search the right half
            if total <= n:
                return search(mid+1, right, n)
            # too many coins, search the left half
            else:
                return search(left, mid, n)

        val = search(left, right, n)
        return val