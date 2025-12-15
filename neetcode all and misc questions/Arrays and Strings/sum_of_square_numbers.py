class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        brute force
        2 for loops
        square both selections and see if they equal c
        O(C^2)

        A slight optimization we can make to bring this from O(C^2) to O(C)
        is recognizing our constraint condition on our two for loops

        note that a^2 + b^2 = c, we don't necessarily have to go all the way to c,
        but instead to the square root of c, so in one loop, 0 -> sqrt(c) and the inner loop,
        0 -> sqrt(c).
        Then, we apply the same logic of checking i**2 + j**2 == c in the nested loop

        To optimize the time even further, you can use a hashset to store all the squared numbers of 
        b, and then perform a loop to only find the values of a^2, and then finding whether
        the difference of c and the a^2 exists in the hashset (similar concept to two sum).

        This optimizes the algorithm to O(Sqrt(N)) time, with O(N) space
        """
        import math
        end = int(math.sqrt(c)) + 1
        squares = set()
        for i in range(0, end):
            squares.add(i**2)
        for j in range(0, end):
            if c-(j**2) in squares:
                return True
        return False