class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Concept:
        Hashmaps
        Create the lookup dicts for balloon, and for the text string,
        only get the characters that exist in the word "balloon"

        if the length of the keys in lookup and textLookup aren't the same,
        that means we don't have all the characters necessary to form the word "balloon", so return 0

        repeatedly subtract the count from each key in lookup dict, if all values are >= 0,
        that means we have successfully formed the word "balloon", so increment by 1

        If at any point, the count of any characters necessary drops below 0, that means we didn't fully
        form the word balloon, so we break and return the count

        """
        from collections import Counter
        lookup = Counter("balloon")
        textLookup = dict()
        for i in range(len(text)):
            if text[i] in lookup:
                if text[i] in textLookup:
                    textLookup[text[i]] += 1
                else:
                    textLookup[text[i]] = 1
        if len(lookup.keys()) != len(textLookup.keys()):
            return 0
        
        count = 0
        while (True):
            textLookup["b"] -= 1
            textLookup["a"] -= 1
            textLookup["l"] -= 2
            textLookup["o"] -= 2
            textLookup["n"] -= 1
            if (textLookup["b"] >= 0 and textLookup["a"] >= 0 
                and textLookup["l"] >= 0 and textLookup["o"] >= 0
                and textLookup["n"] >= 0
               ):
                count += 1
            else:
                break
        return count
        