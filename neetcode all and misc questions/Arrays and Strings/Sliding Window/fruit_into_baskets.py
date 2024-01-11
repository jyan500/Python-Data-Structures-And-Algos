class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Brute Force solution O(N^2)
        2 loops
        1) pick fruit starting from the 0 tree, then 1, etc
        2) keep a dict tracking the amount of each type of fruit

        The problem with this is the repeated work, where we may start at a point
        where we know for certain we're not going to get a bigger answer.
        See below for the more optimized sliding window solution

        """
        # baskets = dict()
        # res = float("-inf")
        # for i in range(len(fruits)):
        #     for j in range(i, len(fruits)):
        #         # pick fruit
        #         if fruits[j] not in baskets:
        #             if len(baskets.keys()) < 2:
        #                 baskets[fruits[j]] = 1
        #             else:
        #                 break
        #         else:
        #             baskets[fruits[j]] += 1
        #     res = max(sum(list(baskets.values())), res)
        #     baskets = dict()
        # return res

        """
        Sliding Window Solution
        Once we see a fruit i that's a different type,
        we set the index.
        Once we exceed our basket length of 2, we can 
        start a recount starting at the first instance of the 2nd fruit i that we found
        
        0, 1, 2, 2
        
        0, 1 is the first window, we start a recount at index 1 (1)
        1, 2, 2 is the second window
        
        returns 3
        
        1, 3, 3, 4, 2, 2, 2
        
        1, 3, 3 is one window (res of 3),
        
        we then start a recount at i = 1 where we first found the fruit 3
        
        3, 3, 4 is the 2nd window (res of 3)
        
        start a recount at the first occurrence of fruit 4 (i = 3),
        
        4, 2, 2, 2 is the 3rd window (res of 4)
        
        returns 4
        
        Time Complexity: 
        O(N)
        Space:
        O(2) (for 2 fruits max in the set)
              
        """

        prevFruitIndex = 0
        baskets = set()
        res = float("-inf")
        cur = 0
        i = 0
        while i < len(fruits):
            if fruits[i] not in baskets:
                if len(baskets) < 2:
                    baskets.add(fruits[i])
                    prevFruitIndex = i
                    cur += 1
                else:
                    res = max(cur, res)
                    # reset the basket starting at the first index that we found the "2nd"
                    # type of fruit in our basket
                    cur = 0
                    i = prevFruitIndex
                    baskets = set()
                    continue
                    
            else:
                cur += 1
            
            i += 1
        
        # if we were able to count all fruits, set the res here 
        # i.e [1, 2, 2]
        
        res = max(cur, res)
        return res
            
        