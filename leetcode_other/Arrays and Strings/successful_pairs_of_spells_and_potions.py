class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # brute force O(N^2)
        # successful = [0 for i in range(len(spells))]
        # for i in range(len(spells)):
        #     numSuccess = 0
        #     for j in range(len(potions)):
        #         if spells[i] * potions[j] >= success:
        #             numSuccess += 1
        #     successful[i] = numSuccess
        # return successful
        
        """
        Using Binary Search
        if we sort the value of potions in ascending order first,
        within our binary search:
            if spell[i] * potions[mid] >= success:
                because it's sorted in ascending order, we know that any number
                after mid will automatically be greater, so we don't need to search there
                we can search the left side
            if spell[i] * potions[mid] < success:
                search the right side instead
                
            When the binary search ends (left >= right)
            
            this is the "threshold" where no potions to the left of left (and left itself)
            will be successful, so the amount of successful potions is just the length
            minus the amount of unsuccessful potions

            success potions = len(potions) - left
        
        this improves our time complexity from O(N^2) to ONLogN

        technically there are m spells, and n potions,
        so it's mlogn + nlogn, because nlogn is the initial sort of the potions,
        and mlogn is the binary search portion, done for each spell 
            
        """
        potions.sort()
        successful = [0 for i in range(len(spells))]
        
        def search(left, right, spell, potions, success):
            mid = left + (right-left)//2
            res = spell * potions[mid]

            if left >= right:
                """
                this is the "threshold" where no potions to the left of left (and left itself)
                will be successful, so the amount of successful potions is just the length of potions
                minus the amount of unsuccessful potions
                """
                # we also need to figure out whether this potion we're on is successful in order to 
                # figure out which side of the boundary we're on. If we're at the last "unsuccessful"
                # potion, we need to subtract 1 
                # 1 2 3 4 5, spell is 1, once the left reaches to 5 (index 4), you'd get len(potions) - left
                # which is 1, but need to subtract an additional 1 to get 0 since no potions should've been successful here
                if spell * potions[left] < success:
                    return len(potions) - left - 1
                else:
                    return len(potions) - left
            if res >= success:
                """ 
                    if successful, we know that any number
                    after mid will automatically be successful too, so we don't need to search there
                    we can search the left side
                """
                return search(left, mid, spell, potions, success)
            else:
                """ if the potion isn't successful, we need a greater number, search the right side """
                return search(mid+1, right, spell, potions, success)
        
        for i in range(len(spells)):
            successful[i] = search(0, len(potions)-1, spells[i], potions, success)
        return successful
                
            