class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Revisited 10/30/2024
        """
        from collections import defaultdict
        c = defaultdict(int)
        for i in range(len(s)):
            # ensure that we have at least 10 characters to slice
            if i + 10 <= len(s):
                sequence = s[i:i+10]
                c[sequence] += 1
        return [key for key in c if c[key] > 1] 

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        https://leetcode.com/problems/repeated-dna-sequences/
        
        A A A A A C C C C C A  A  A  A  A  C  C  C  C  C  C  A  A  A  A  A  G  G  G  T  T  T
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
  
        Current Brute Force:
        O((10*N)*N)
        1) Outer loop goes through each index i of string S
           inner loop goes through each subsequent substring starting from index i of length 10
        
        2) Have a set that records the sequence and the index
            (string, index)
            if the same sequence shows up with the same starting index, do not count this
        
        3) Otherwise, record the repeated sequence in the counter dict
        
        We end up repeating a lot of work by revisiting the same sequence at the same index by doing
        two for loops
        
        Slightly Optimized:
        O(N * 10)
        Instead of storing the sequence and index in the indexmap, we can actually just store the index,
        because we don't want to count sequences starting from an index we've already visited.
        
        This way, we can add this condition before the nested loop, so we can avoid re-visiting indices
        we've already visited
        
        This passes the runtime test, memory could probably be optimized.
        
        Even More Optimized 
        (https://leetcode.com/problems/repeated-dna-sequences/discuss/53855/7-lines-simple-Java-O(n))
        
        The key realization is that to a we only need one loop, we can cover all possibilities by simply iterating from 
        i ... i + 9, as any indices past this won't make a full 10 length sequence. 
        
        This way, at every i, we simply take the substring 
        from s[i:i+10] (not counting the last char), so don't run into the issue of double counting the indices like before with two loops, so we don't need the index map.
        
        
        
        
        
        A A A A A C C C C C A  A  A  A  A  C  C  C  C  C  C  A  A  A  A  A  G  G  G  T  T  T
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
        
        counter
        1st iteration,
        i = 0
        substring from 0 to 9
        A A A A A C C C C C
        
        {A A A A A C C C C C: 1}
        
        2nd iteration,
        i = 1
        substring from 1 to 10
        A A A A C C C C C A
        
        {A A A A A C C C C C: 1,  A A A A C C C C C A: 1}
        
        3rd iteration,
        i = 2
        substring from 2 to 11
        A A A C C C C C A A
        
        {A A A A A C C C C C: 1,  A A A A C C C C C A: 1,  A A A C C C C C A A: 1}
        
        4th iteration
        i = 3
        substring from 3 to 12
        {A A A A A C C C C C: 1,  A A A A C C C C C A: 1,  A A A C C C C C A A: 1, A A C C C C C A A A : 1}
        
        5th iteration
        i = 4
        substring from 4 to 13
        {
           A A A A A C C C C C: 1,  
           A A A A C C C C C A: 1,  
           A A A C C C C C A A: 1, 
           A A C C C C C A A A : 1,
           A C C C C C A A A A : 1, 
           }
        
        6th iteration
        i = 5
        substring from 5 to 14
         {
           A A A A A C C C C C: 1,  
           A A A A C C C C C A: 1,  
           A A A C C C C C A A: 1, 
           A A C C C C C A A A : 1,
           A C C C C C A A A A : 1, 
           C C C C C A A A A A : 1,
           }
        
        ...
        
        At i = 10, we can see A A A A A C C C C C become repeated
              {
           A A A A A C C C C C: 2,  
           A A A A C C C C C A: 1,  
           A A A C C C C C A A: 1, 
           A A C C C C C A A A : 1,
           A C C C C C A A A A : 1, 
           C C C C C A A A A A : 1,
           ...
           }
        ...
        at i = 16, we can see C C C C C A A A A A become repeated
         {
           A A A A A C C C C C: 2,  
           A A A A C C C C C A: 1,  
           A A A C C C C C A A: 1, 
           A A C C C C C A A A : 1,
           A C C C C C A A A A : 1, 
           C C C C C A A A A A : 2,
           ...
           }
        
        """
        # counter = dict()
        # indexMap = set()
        # n = len(s)
        # for i in range(n):
        #     if i not in indexMap:
        #         for j in range(i, n, 9):
        #             if j + 9 < n:
        #                 indexMap.add(j)
        #                 substring = s[j:j+10]
        #                 if substring in counter:
        #                     counter[substring] += 1
        #                 else:
        #                     counter[substring] = 1
        # return [key for key in counter if counter[key] > 1]
        counter = dict()
        n = len(s)
        for i in range(n):
            if i + 9 < n:
                substring = s[i:i+10]
                if substring in counter:
                    counter[substring] += 1
                else:
                    counter[substring] = 1
        return [key for key in counter if counter[key] > 1]