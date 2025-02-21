class Solution:
    """
    https://neetcode.io/problems/string-encode-and-decode
    in order to handle cases where the delimited strings
    may have any form of delimiter (which means it's not safe to
    assume a special character can be used as a delimiter), mark
    the beginning of each string with it's length, followed by a "#", and use that
    as a delimiter. So when it's converted back to a list, we iterate
    through the string until we reach a "#", forming a number. Then, we
    slice the string based on the length of the number we created.

    Another reason to include a "#", is to handle edge cases like so:
    [""], which should return [""]
    you would get "0#" as the encoded string.
    If you didn't include the "#", you'd get "0". The issue is that if you don't include
    the delimiter, there's nothing after the "0" to parse, so you'd end up with an empty
    array.
    Whereas with "0#", after parsing 0, the slicing of the string after "#" would result
    in an empty string.
    for example:
    s = "0#"
    cur = 0
    i = 1
    segment after the "#" is s[i+1:i+cur+1]
    when slicing from
    s[2:2], you'd get "", since you can't slice out of bounds
    """
    def encode(self, strs: List[str]) -> str:
        res = []
        for i in range(len(strs)):
            res.append(str(len(strs[i]))+"#")
            res.append(strs[i])
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        N = len(s)
        res = []
        i = 0
        cur = 0 
        while i < N:
            # continue looping until we reach a "#", this is to handle
            # edge cases where the length of one of the substrings is greater than 9
            if s[i].isnumeric():
                cur = (cur * 10) + int(s[i])
                i += 1
            elif s[i] == "#":
                # include the next string up to i + cur + 1 (which includes the last character)
                segment = s[i+1:i+cur+1]
                res.append(segment)
                i = i + cur
                # reset cur
                cur = 0
                i += 1
        return res