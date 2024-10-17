class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Monotonic Stack based solution
        O(N) Time
        O(N) Space
        https://youtu.be/cFabMOnJaq0
        The key is to keep a monotonic stack where the values are strictly increasing.
        So whenever the top of the stack is greater than the current element, we have to continue popping until it's < current element
        However, each pop will be considered one removal from the string, which would decrement k as well.
        
        The observation which would suggest a monotonic stack is that when looking at a number and determining which digits
        to remove, if we see a number with strictly increasing digits like 1 2 3 4 5, removing numbers from the right side
        will always result in the smallest possible number. Whereas for numbers with strictly decreasing digits (i.e 5 4 3 2 1),
        you'd remove numbers from the left side.
        
        When faced with a situation where you have two of the same digit in a number, you'd favor removing the one on the left side
        to product the smaller number. For example, 4 5 3 2 5, removing the 5 at index 1 would result in 4 3 2 5, whereas
        removing the on on the right most would result in 4 5 3 2, which is larger.
        
        By using a stack, we build up a number, including digits only in increasing order, and then do the "removals" if we 
        see a number that's less than the top of the stack. In the edge case where after this process, k is still > 0,
        (i.e if we have a monotically increasing number)
        we'd have to do a second step to "pop" off the top of the stack (right side), until k = 0
        
        4 4 3 2 2 1 9, k = 3
        
        stack = [4]
        stack = [4, 4] (still okay)
        next number is 3, we need to pop 4 to keep the values strictly increasing, and the previous 4 as well. k decrements to 1 since
        we did 2 removals here.
        stack = [3]
        next number is 2, we need to pop 3 to keep the value strictly increasing
        k decrements to 0
        stack = [2]
        next number is 2 (still okay)
        stack = [2, 2]
        next number is 1, but we can't remove any more numbers since k = 0
        stack = [2, 2, 1]
        next number is 9
        stack = [2,2,1,9]
        
        Now in the case of an already monotonically increasing number
        1 2 3 4 5, k = 3
        we'd have [1,2,3,4,5] onto our stack
        
        and then we'd need to perform k amount of pops to receive the smallest number
        
        1 2 is the smallest after popping 3 4 5
        
        There's also two more edge cases with leading zeroes, after producing the stack,
        and popping out all necessary elements, while parsing and creating the result string,
        set the flag to only include the first non-zero element and any remaining after.
        
        If the string remains empty, return "0", otherwise return the string
        
        """
        stack = []
        for c in num:
            n = int(c)
            while (stack and k > 0 and n < stack[-1]):
                stack.pop()
                k-=1
            stack.append(n)
        if k > 0:
            for i in range(k):
                stack.pop()
        res = ""
        # we need to remove any leading zeroes
        # by using a flag set to False, once a non-zero value is reached, that value will be
        # set to true, and any other value after should be included.
        # for example 00230,
        # the flag will be set to True once 2 is reached, so anything after (i.e 3 and 0) should be included
        seen = False
        for i in range(len(stack)):
            if stack[i] != 0:
                seen = True
            if seen:
                res += str(stack[i])
        return "0" if not res else res
        """
        cannot contain leading zeroes
        if all digits are removed, then it will default to "0"
        
        Brute Force:
        Find all possibilities of numbers after 3 digits are removed using backtracking
        Find the minimum
        
        Note that the sys.set_int_max_str_digits(0) is only there to allow for conversions of numerical strings with len > 4300 to integers
        
        Exponential Time Solution (TLE's on case 23)
        """
        """
        import sys
        sys.set_int_max_str_digits(0)
        self.N = len(num)
        self.currentMin = float("inf")
        def search(cur, removalsRemaining):
            if cur == "":
                self.currentMin = "0"
                return
            if removalsRemaining == 0:
                self.currentMin = min(int(cur), self.currentMin)
                return
            for i in range(len(cur)):
                search(cur[:i] + cur[i+1:], removalsRemaining - 1)
        search(num, k)
        return "0" if self.currentMin == float("inf") else str(self.currentMin)
        """
                
                