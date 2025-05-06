"""
Binary Search on a range of numbers

1) Determine the lower and upper bound first for an optimization problem like this, we ask ourselves,
what's the minimum amount we could try, even if it doesn't meet the requirements? And then what's the maximum
we could try, which would certainly meet the requirements of the problem?

https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
Similar to:
Minimum limit of balls in bag
https://www.youtube.com/watch?v=MQlC8EoOdZ0&t=528s&ab_channel=NeetCodeIO
"""
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        """
        for example if there are 6 stores, quantities = [11, 6]
        it's possible that you could give all the quantities to one store of a given product,
        and the rest of the stores receive 0
         
        11 6 _
        _  _ _

        therefore,you could say that the upper bound of X is just the maximum amount
        that you could give to one store, which is max(quantities)

        the lower bound of X is 1, because you could just give 1 of each product until the quantity runs out

        i.e you could distribute the 11 across each of the 6 stores by giving 1 to each store
        1 1 1 
        1 1 1, 
        however, because of the rule that each store can only receive one of each 
        product type, you can see that giving 1 of each isn't going to work here, because
        we run out of stores before we're able to distribute all 11 of the quantity.

        Essentially, we're asking ourselves, what's the max amount of product we could give to each store, such that we're able to distribute all the quantity of that product to N stores. 

        for example, we saw that distributing 1 of each doesn't work. a max of 2 could work ...
        distributing 11 where the max is 2
        2 2 2
        2 2 1
        distributing 6 whre the max is 2
        2 2 2
        _ _ _, adding this together with the distribution of the 11 would be ...
        4 4 4
        2 2 1
        So the max product quantity of a given store is 4

        As a mathematical property, given the current bounds we want, perform ceil(quantity/maxQuantity) to get the most optimal amount that can be given to each store, this is to see if we are able to distribute all products
        to the given amount of stores

        We can do linear scan on the range of numbers to start, but this can be optimized
        with binary search as well.
        """
        from math import ceil
        lowerBound = 1
        upperBound = max(quantities)

        def canDistribute(maxQuantityInOneStore):
            numStores = 0
            for i in range(len(quantities)):
                # this calculates the amount of stores that are needed
                # to distribute this max amount of product to a given store
                numStores += ceil(quantities[i]/maxQuantityInOneStore)
                if numStores > n:
                    return False
            return True
        
        # perform binary search 
        def binarySearch(l, r):
            # if we've exceeded the search space, that means we should be as 
            # close to optimal as possible, where l should represent the smaller number,
            # which is what we're looking for since we want the minimal amount of products
            # needed in a given store
            if l >= r:
                return l

            mid = l + (r-l)//2

            # search left to see if we can find a better answer in the case
            # we're able to distribute using mid, which represents a given amount of product
            if canDistribute(mid):
                return binarySearch(l, mid)
            else:
                return binarySearch(mid+1, r)

        return binarySearch(lowerBound, upperBound)
        



