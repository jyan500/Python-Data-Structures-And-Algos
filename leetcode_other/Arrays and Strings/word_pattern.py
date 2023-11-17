class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Very similar to Leetcode "Isomorphic Strings" problem
        
        Time Complexity: O(N) Space: O(N)
        
        Concept:
        1) Using a hashmap, we map each space-separated word within the string S 
        to it's corresponding character in pattern based on index i, as well as 
        the amount of times this word has been mapped to this character within a tuple like so:
        
        
        {dog: (a, 2), cat: (b, 2)}
        
         a   b   b   a
        dog cat cat dog 
        
        2) We then compare the amount of times the character appears in the string pattern 
        with the amount of times that character has been mapped within our hashmap
            - If the values are the same, that means each space separated word maps
            with it's corresponding character, so return True, else return False
            
        Some edge cases to handle:
        1) Two different words in the string s CANNOT map to the same character in pattern
        i.e 
         a   b   b   a
        dog cat cat fish
        
        both dog and fish are mapping to "a", which is incorrect. To handle this, we keep track of a 
        set of characters we've already mapped, so if we encounter a word we haven't seen yet, but 
        it's corresponding character has already been mapped, we can automatically return False.
        
        2) A word in the string s must map to only one character and cannot be changed later on
        
         a   b   a   b
        dog cat cat dog
        
        note that cat maps to "b", but then in the next index, cat maps to "a",
        this is invalid.
        
        In order to catch this, this is why we store both the character that the word maps 
        to, as well as the amount in tuple like so:
        
         {cat: (b, 1)}
         
         if we were try to add cat back in, it would notice it's already been mapped to "b"
         since "a" != "b", return False.
         Otherwise, we can add this in, and increment 1 to 2 (say if "cat" was mapping with another "b" rather than "a")
        
        
        """
        from collections import Counter
        words = s.split()
        
        lookup = Counter(pattern)
        mapped = dict()
        alreadyMapped = set()
        if len(pattern) != len(words):
            return False
        for i in range(len(words)):
            if words[i] not in mapped:
                # we cannot map the same word to the same character in 
                # "pattern" string twice
                if pattern[i] not in alreadyMapped:
                    mapped[words[i]] = (pattern[i], 1)
                    alreadyMapped.add(pattern[i])
                else:
                    return False
            else:
                char, amt = mapped[words[i]]
                # if the character that was mapped to words[i] earlier
                # is different, this cannot be valid
                if char != pattern[i]:
                    return False
                else:
                    mapped[words[i]] = (pattern[i], amt + 1)
        return list(lookup.values()) == [amt for char, amt in mapped.values()]
        