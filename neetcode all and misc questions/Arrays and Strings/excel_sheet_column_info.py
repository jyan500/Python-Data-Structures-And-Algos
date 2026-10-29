class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """ 
        mod to get the last digit first, then integer division by 26 to move onto the next digit
        The tricky part about this problem is that there's an off-by-one error since
        the letters in the column title are 1 - 26, but when doing mod 26, this would actually
        map 0 to 25 instead. For example, 26 % 26 = 0, which should evaluate to "Z" instead of "A".
        To account for this, we have to subtract 1 from the original number before performing the mod,
        AND also before doing the quotient.
        for example:

        letters are mapped 0: A, 1: B, ... 25: Z
        orig = 728
        (728-1) % 26 = 727 % 26 = 25, this maps to Z
        (728-1) // 26 = 27
        (27-1)%26=0, this maps to A
        (27-1)//26=1
        (1-1)%26 =0, this maps to A
        (1-1)//26=0

        final result is AAZ

        """
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        record = {}
        for i in range(len(letters)):
            record[i]=letters[i]
        res = [""]
        orig = columnNumber
        while orig > 0:
            last_digit = (orig - 1) % 26
            res = [record[last_digit]] + res
            orig = (orig - 1) // 26
        return "".join(res)