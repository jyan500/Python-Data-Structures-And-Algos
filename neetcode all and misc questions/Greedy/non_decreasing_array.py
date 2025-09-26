class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        At first I tried to come up with a monotonic stack solution but this wasn't the right approach,
        because you need to consider the surrounding elements and not just maintaining the order.

        Greedy solution:
        (From Claude)
        Core Algorithm

        Scan for violations: Look for positions where nums[i-1] > nums[i]
        Count violations: If more than one violation exists, return false immediately
        Fix the violation: When we find a violation, we have two options for fixing i

        Decision Logic
        When we find nums[i-1] > nums[i], we need to decide:
        Option 1: Lower nums[i-1] to nums[i]

        This works if i == 1 (first element) OR nums[i-2] ≤ nums[i]
        We can safely make this change without creating a new violation

        Option 2: Raise nums[i] to nums[i-1]

        We do this when Option 1 would create a new violation
        This happens when nums[i-2] > nums[i]

        Key Edge Cases

        Arrays with length ≤ 2 are always fixable
        When the violation is at the beginning or end, we have more flexibility
        Multiple violations mean it's impossible to fix with just one change

        An example:
        -1 4 2 3

        The first violation is reached at i = 2 (value of 2)
        here we can see the two choices we have:
        either
        1) Decrease nums[i-1] to be nums[i]'s value
        OR
        2) Increase nums[i] to be nums[i-1]'s value

        This is where the greedy approach comes in, we always try to do option 1) first because
        it decreases the chance of creating another violation later on.

        So if we do option 1) we would get
        -1 2 2 3, which is correct
        but if we were to do option 2), we would get
        -1 4 4 3, which creates another violation at i = 3 since 3 < 4

        However in this example, we can't perform option 1
        [4,4,2,5], this is because in the first violation i = 2
        nums[i-2] is NOT less than nums[i], since 4 > 2 and not less than

        so trying to lower nums[i-1] to nums[i] value would just create another violation,
        we so we have to option 2), which is raising nums[i] to nums[i-1] value like so:
        4 4 4 5
        
        this would be a correct answer
        """
        violations = 0
        for i in range(1, len(nums)):
            # if the sequence is decreasing,
            # this is a violation
            if nums[i-1] > nums[i]:
                violations += 1
            
                # can't have more than one violation,
                # return false
                if violations > 1:
                    return False
                
                # Case 1: Modify nums[i-1] (make it smaller)
                # This works if either:
                # i == 1 (no element before i-1), OR
                # nums[i-2] <= nums[i] (won't create new violation)
                # for example: i = 2, [2, 4, 3]
                # we can fix the violation here by changing 4 to 3,
                # since nums[i-2] <= nums[i] (2 <= 3)
                # this way you get [2, 3, 3], which is non-decreasing.
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                # Case 2: Modify nums[i] (make it larger)  
                # If we can't do Case 1, we must do this
                else:
                    nums[i] = nums[i-1]
        return True
            
        
                
            