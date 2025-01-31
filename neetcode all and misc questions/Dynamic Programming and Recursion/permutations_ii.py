class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        For permutations, 
        pick i, and then limit the subspace to any other elements
        other than i
        [1, 1, 2]
        picks i = 0, 
        so the remaining space is [1,2]

        [1,2], picks i = 0, looking at the original nums list [1, 1, 2],
        since we now picked the middle "1", only the last element [2] is available

        To avoid duplicates,
        you could place the elements in a tuple, and then place the permutation in a set
        to avoid duplicate permutations
        """
        """
        # first solution
        res = set()
        def search(searchSpace: [int], cur: (int)) -> None:
            if len(searchSpace) == 0:
                res.add(cur)
                return
            for i in range(len(searchSpace)):
                # pick the element at i, and recur down the search space that contains
                # every other element besides i (and subsequently, every element that we've chosen previously)
                remainder = searchSpace[:i] + searchSpace[i+1:]
                # add current element to the permutation
                search(remainder, cur + (searchSpace[i],))
        search(nums, ())
        return [list(element) for element in list(res)]
        """
        """
        Neetcode's solution using a hashmap to avoid duplicates
        https://youtu.be/qhBVWf0YafA
        1) instead of using the array, convert the array into a hashmap counter of each element
        As you choose elements, you decrement the count in the hashmap. After backtracking,
        you would re-increment the count to allow for other potential paths

        for example: [1,1,2] becomes {1: 2, 2:1}

        call1: when performing backtracking, you can pick 1, decrementing to {1:1, 2:1}
        call2: then in the next call, you can pick 1 again {1: 0, 2: 1}. 

        call3: Now you can't pick 1, only 2, to get 1 1 2

        backtracking ...
        call2: {1:1, 2:1}, you can pick 2 instead of 1, so you'd get 1 2,
        call4: then {1:1, 2:0}, to pick 1 again and get 1 2 1

        call2: backtracking all the way to {1:1, 2:1}, we've exhausted all possibilities here,

        backtrack to call1, {1:2, 2:1}, because we've already chosen "1", since we're looping over
        the hashmap keys, since we've already picked 1, the only other possiblity is
        to pick 2. 

        call5: picks 2 to get [2], {1:2, 2:0}
        call6: picks 1 to get [2,1], {1:1, 2:0}
        call7: picks 1 to get [2,1,1], {1:0,2:0}

        these are all the results: [1,1,2], [1,2,1], [2,1,1]

        Time Complexity: O(N!) , I'm not too sure about this myself
        Space: O(N) for the hashmap
        """
        from collections import Counter
        counter = Counter(nums)
        res = []
        def search(cur):
            if len(cur) == len(nums):
                res.append(cur)
                return
            for key in counter:
                if counter[key] > 0:
                    counter[key] -= 1
                    search(cur + [key])
                    counter[key] += 1
        search([])
        return res
        

            