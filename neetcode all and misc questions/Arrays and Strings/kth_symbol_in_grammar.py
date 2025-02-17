class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        https://leetcode.com/problems/k-th-symbol-in-grammar/
        https://neetcode.io/solutions/k-th-symbol-in-grammar

        n=1 0
        n=2 01
        n=3 0110
        n=4 01101001

        [0]
        [0, 1]
        [0, 1, 1, 0]

        This is a tricky question that doesn't follow a specific pattern!

        Brute Force approach:
        --------------------------------
        1) initialize a res list that will store each "level"
        of the row, starts out at [[0]], since at n = 1,
        it's just one zero
        2) Store an index (i.e listIndex) that keeps track
        of the previous row in our res list
        3) Iterate through n, and then for each level,
        look at the row in res list, and then perform the 
        replacement operations, appending to a new array. 
        4) Append the new array to res list and then
        increment listIndex so we're looking at the right level
        for the next iteration

        This gets memory exceeded on LC, likely because
        we don't need to store the actual elements in a list 

        Time: O(2^N-1)
        Space: O(2^N-1)

        Optimal approach:
        --------------------------------
        Because we're looking for the element K,
        we can perform a binary search to find that specific element
        by treating each row like a tree
            0
          0   1
        0  1 1  0
             ^

        So if we wanted n = 3, and k = 3, you'd use binary search to find
        1. 

        Essentially, we just keep a variable that sets itself to 0 or 1
        at each level.

        Time: O(K), the height of the tree
        Space: O(1)

        Example execution:
        since n = 3, there is n - 1 iterations (0, 1, 2)

        1st iteration 
        cur = 0
        left = 1, right = 2^(3-1) = 4
        mid = 1 + (4-1)//2 = 1 + 3//2 = 2
        k is greater than mid, since 3 > 2, so we have to search the right half
        swap 0 to 1
        left = mid + 1

        2nd iteration
        cur = 1
        left = 3, right = 4
        mid = 3 + (4-3)//2 = 3 + 1//2 = 3
        k <= mid, since k = 3 and mid = 3
        search the left side, 
        right = mid

        3rd iteration
        cur = 1
        left = 3 right = 3
        mid = 3 + (3-3)//2 = 3 + 0 = 3
        k <= mid, since k = 3 and mid = 3
        search the left side

        binary search ends, and cur = 1, which is the answer
        """

        # Brute Force, building up and storing each layer
        """
        res = [[0]]
        listIndex = 0
        for i in range(1, n):
            level = []
            for j in range(len(res[listIndex])):
                element = res[listIndex][j]
                if element == 0:
                    level.append(0)
                    level.append(1)
                if element == 1:
                    level.append(1)
                    level.append(0)
            res.append(level)
            listIndex += 1
        desiredList = res[n-1]
        return desiredList[k-1]
        """
        """ 
           Optimal: binary search
        """
        cur = 0
        # notice that right is the max width that the tree could have
        left, right = 1, 2**(n-1)
        for _ in range(n-1):
            mid = left + (right-left)//2
            # if k <= mid, it's in the left half,
            # set the right boundary to mid so you're moving to the left
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                """
                if you move to the right,
                notice 
                   0
                  0  1
                  
                   1
                  1  0
                in the next row, you can see that
                if you move to the left, the next number
                is always the same, but when moving to the right,
                the number is swapped (0 to 1, or 1 to 0)
                """
                cur = 0 if cur == 1 else 1
        return cur
