class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        https://www.youtube.com/watch?v=fJaKO8FbDdo&ab_channel=takeUforward
        Approach:
        Starting from the back and working towards the beginning of both strings,
        defining i as length of word1 and j as the length of word2
        
        At each point we have three different operations
        insert
        replace
        delete
        
        we want to run recursion and find the minimum
        between the three operations
        
        When defining the recurrence relation, we think about comparing the characters
        of both strings at points i, j and how the operations affect this
        
        insert:
        assuming i = 4
        j = 2
        horse
        ros
        
        say if we insert s 
        horses
        ros
        
        i remains at 4, because we've now matched the hypothetical character "s"
        that we just inserted with the "s" at j = 2, we can now shift by one to the left
        
        therefore, insert = f(i, j-1)
        
        delete:
        assuming i = 4
        j = 2
        horse
        ros
        
        if we delete e, we still need to match "s", so i shifts by one and j stays the same
        
        in this case,
        i is now 3, and s now matches
        therefore, delete = f(i-1, j)
        
        replace:
        assume i = 4
        j = 2
        horse
        ros
        
        if we replace e with s,
        we need to shift both indices i and j, since i and j both match, so we can move onto the remainder of the string
        
        Base Cases:
        
        If we've decreased the index to the point where word1 is now an empty string, and there are still characters for word2,
        it takes len(word2) insert operations to take an empty string to word2, therefore:
        
        return j + 1
        
        since j is length of word2 - 1, so we add back the 1
        
        if we've decreased the index to the point where word2 is now an empty string, and there are still characters for word1,
        it takes len(word1 insert operations to take an empty string to word1, therefore
        
        return i + 1
        
        since j is length of word1 - 1, so we add back the 1
        
        If both the characters at word1 and word2 are the same, then no operations are needed, but we shift both i and j by one
        
        return f(i-1, j-1)
       
       	-------------------------------

       	We can then use memoization to store our results as (i, j) to cut down
       	on repeated subproblems
	
		Without memoization, the time complexity would be exponential (3^N)
       	Final Time Complexity: O(N*M)
       	Space Complexity: O(N*M)
        """
        self.memo = dict()
        def f(i, j, word1, word2):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if (i,j) in self.memo:
                return self.memo[(i,j)]
            if word1[i] == word2[j]:
                self.memo[(i,j)] = f(i-1, j-1, word1, word2)
                return self.memo[(i,j)]
            insert = f(i, j-1, word1, word2)
            replace = f(i-1,j-1, word1, word2)
            delete = f(i-1,j, word1, word2)
            # in our recurrence relation, we want to find the operation that results in the minimal
            # amount of total operations needed, so we take the min between these three
            # the addition of 1 represents that at this particular step, we need to do at least one operation.
            self.memo[(i,j)] = 1 + min(insert, replace, delete)
            return self.memo[(i,j)]
        
        return f(len(word1)-1,len(word2)-1, word1, word2)
        