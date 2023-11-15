class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        O(N) Time O(N) Space

        Key Concept:
        Try to transform the string based on the characters that you've seen
        using a hashmap to keep track of the mappings. Once we've seen a character,
        we continually use that character to map and replace.

        if the transformed result is not equal to t, that means the answer is False

        e g g 
        a d d 

        e maps to a, dict = {e: a} set = {a}

        g maps to d, dict = {e: a, g: d} set = {a, d}

        g maps to d

        b b b a a a b a
        a a a b b b b a

        b maps to a, dict = {b: a}, set = {a}
        b maps to a, dict = {b: a}, set = {a}
        b maps to a, dict = {b: a}, set = {a}

        a maps to b, dict = {b: a, a: b}, set = {a, b}
        a maps to b, dict = {b: a, a: b}, set = {a, b}
        a maps to b, dict = {b: a, a: b}, set = {a, b}

        b maps to a, dict = {b: a, a: b}, set = {a, b}
        a maps to b, dict = {b: a, a: b}, set = {a, b}

        the final result is:
        a a a b b b a b, not equal to: 
        a a a b b b b a

        return false

        you need an additional condition that states that no two characters can map to the same character.
        We can keep track of a separate "mapped" set, so whenever we map a character in our charMap,
        we add that to our mapped set.

        b a d c
        b a b a

        b maps to b, a maps a 
        dict = {a: a, b: b}
        set = {a, b}

        If we try to add d to our dict,
        d cannot map to b, because b has already been mapped according to our set,
        so we automatically return False here.
        
        """
        
        i = 0
        j = 0
        res = ""
        charMap = dict()
        mapped = set()
        while (i < len(s) and j < len(t)):
            if s[i] not in charMap:
                if t[j] not in mapped:
                    charMap[s[i]] = t[j]
                    mapped.add(t[j])
                else:
                    return False
            # once we've found the character to map over from t,
            # always use the same character to replace it
            res += charMap[s[i]]
            i += 1
            j += 1
        return res == t