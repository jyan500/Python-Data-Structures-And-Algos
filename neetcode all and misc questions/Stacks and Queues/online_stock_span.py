class StockSpanner:
    """
    Solution that I came up with on 7/17/2025

    A brute force solution would be to iterate backwards on each price to find the number
    of consecutive days where price <= number

    Optimized:
    monotonic stack problem (similar to daily temperatures)

    keep array of all values, and then keep stack of values that are strictly decreasing
    if our current value is greater than the top of the stack, pop out of the stack, but also
    keep track of how many values were less than the current value in a tuple. If we're popping out, 
    we can add the amount of values before it to the initial starting number of 1 (which says there's
    1 consecutive day which is the current day)

    7 (no value before it, 1)
    2 (this is strictly decreasing, 1)
    1 (this is also strictly decreasing, 1)
    2 (this is not strictly decreasing, initialize as 1, pops out, adds value of 1 to 2)

    becomes

    7
    2
    2 (not strictly decreasing, adds value to 3)

    7
    2 (has value of 3 to show 3 values less than that came before it)

    7 (1)
    2 (3)
    adds value 8 (initialize to 1, no longer strictly decreasing)
    pops out 2, but this time add the value 3 to the initial value 1, which shows
    that its been at least 4 consecutive days with price on stack <= current

    7 (1)
    8 (4),
    still not strictly decreasing, pops out 7 and adds 1 to the value, for total of 5

    Time: Each next() call should be at worst O(N)
    Space: O(N)

    """
    def __init__(self):
        # stores a tuple where the (price, number of consecutive days where the current price <= top of the stack)
        self.stack = []

    def next(self, price: int) -> int:
        numDays = 1
        while (len(self.stack) > 0):
            # store the amount of consecutive days where the current value >= top of the stack
            topPrice, numConsecutiveDays = self.stack[-1]
            # if we have a price that's greater than the top of the stack, we include the amount
            # of consecutive days that we saved into our running total (numDays)
            # so we don't need to re-calculate those values again.
            if price >= topPrice:
                self.stack.pop()
                numDays += numConsecutiveDays
            # because we're keeping a monotonic decreasing stack, if we see a value that's greater,
            # we can't pop out anymore, so we break.
            else:
                break
        # finally, save the price along with the number of consecutive days where price >= top of stack
        self.stack.append((price, numDays))
        return numDays


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.res = []

    def next(self, price: int) -> int:
        """ 
            original solution:
        
            1) storing the original indices in the tuple within the stack,
            and then finding the difference between the indices
            2) the issue was that if we had a list of numbers where each number was
            strictly increasing in value, the stack would be empty, so I'd have to 
            subtract -1 off the index value of the current price to get the right answer
            
            Neetcode solution:
            https://www.youtube.com/watch?v=slYh0ZNEqSw&ab_channel=NeetCode
            
            1) Rather than storing the indices in the tuple within the stack,
            you can just store the range instead.
            
            a) next(70)
            input: 100 80 60 70 60 75 85
            
            stack = [(100, 1), (80, 1), (60, 1)]
            
            100 80 60 70 60 75 85
                       ^
            starting at 70...
            At 70, because 60 is less, we can add 1 to our current span of 1,
            which would be 2, and then pop 60
            
            b) next(60)
               
            [(100, 1), (80, 1), (70, 2)]

            100 80 60 70 60 75 85
                          ^
            At 60, 60 is less than 70, so we just do a span of 1
            
            [(100, 1), (80, 1), (70, 2), (60, 1)]
            
            
            c) next(75)
            
            100 80 60 70 60 75 85
                             ^
            At 75, 60, 70, and 60 are less
            we pop 60, adds 1 to our span, span = 2
            we pop 70, adds 1 to our span, span = 3
            we pop 60, adds 1 to our span, span = 4
            finally we get to 80, which is not less anymore.
            
            We save (75, 4) into our stack, span is 4
            
            [(100, 1), (80, 1), (75, 4)]
            
            d) next(85)
            100 80 60 70 60 75 85
                                ^
            
            At 85, 75 is less, so we add 4 to our span, span = 5
            pop (75, 4) off the stack
            
            80 is less than 85, so we pop 80 off of our stack, adds
            1 to our span, span = 6
            
            100 is not less than 85, so we stop here
            
            span is 6
            
            
        """
        """
        num = 1
        if len(self.res) == 0:
            self.res.append(price)
            self.stack.append((price, 0))
        else:
            while (len(self.stack) > 0 and price >= self.stack[-1][0]):
                self.stack.pop()
            if len(self.stack) > 0:
                index = self.stack[-1][1]
            else:
                index = -1
            self.res.append(price)
            num = len(self.res)-1 - index
            self.stack.append((price, len(self.res)-1))
                
        return num
        """
        span = 1
        while (len(self.stack) > 0 and price >= self.stack[-1][0]):
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span
        
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)