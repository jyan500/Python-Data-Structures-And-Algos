class Solution:
    """
    O(N) Time
    O(1) Space

    Approach:
    The problem states that we can only use O(1) Space, so can't use hashmap to count the characters which is the normal strategy.
    1) To get around this, keep a sliding window using two pointers, incrementing the right pointer first.
    2) Whenever the left and right pointers values are not equal to each other,
    this means that we've fully visited a group of characters, since we know the input is already grouped by same characters (i.e all the "a"s are next to each
    all "b"s next to each other, etc) 
        At this point, we then do right - left which gives us the count of characters for this group, and then we know we insert
        the character + the count as a string i.e "a2", "b3", etc. We then append each individual character
        of the string to the input array

        If the count of chars is only 1, just input the char

        After this, set l to r to slide the window

    3) After the iteration ends, we have to repeat the process of right - left , append chars, once more since r just exceeded
    the length of the list, but we have to account for the last set of characters

    4) After this, we pop out the characters from the front until we reach the end of our original list size


    Example:
    a a a b b c c d

    save N = 8, which is the original length

    l = 0 
    r = 0

    l = 0
    r = 3
    the characters are different here,
    so 3 - 0 = 3, 3 "a" total
    add "a" and "3" to the original list

    a a a b b c c d a 3
                    _ _

    set l to r

    l = 3 
    r = 3 

    at r = 5
    l = 3,
    r - l = 2,
    we then insert "b" and "2"

    a a a b b c c d a 3 b 2

    set l = r,
    r = 5
    l = 5


    r = 7
    l = 5,

    the characters are different,
    so 7 - 5 is 2, add "2" and "c"

    a a a b b c c d a 3 b 2 c 2

    set l = r, r = 7, l = 7

    note that iteration ends here since r > N, but we still need to account for the last set of characters

    r = 8
    l = 7,

    count of 1, so we only append "d"

    a a a b b c c d a 3 b 2 c 2 d

    we then take only the underlined section by popping the elements out from the front

    a a a b b c c d a 3 b 2 c 2 d
                    _____________
                

    """
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        if N == 1:
            return N
        l = 0
        r = 0
        while r < N:
            # if the characters are not the same, or r is exceeded out of bounds
            if chars[l] != chars[r]:
                count = r - l
                if count > 1:
                    toInsert = chars[l] + str(count)     
                    for i in range(len(toInsert)):
                        chars.append(toInsert[i])
                else:
                    # in the case of only one character, just append that single character
                    chars.append(chars[l])
                l = r
            r += 1
        # account for the last set of characters once r exceeds the length of chars
        count = r - l
        if count > 1:
            toInsert = chars[l] + str(count)
            for i in range(len(toInsert)):
                chars.append(toInsert[i])
        else:
            chars.append(chars[l])
        # remove everything from index 0 to the first point when we started inserting new characters,
        # which is the end of the original list length, by popping off the first character until we reach N
        for i in range(0, N):
            chars.pop(0)
        return len(chars)
        
            