class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        monotonic stack in decreasing order
        the pattern here though is that similar to remove all adjacent duplicates in string II ,
        we track the element in the stack, but also something else, in this case, it's the minimum
        that we've found so far. This helps because as we keep the stack in decreasing order,
        we need to know the minimum element that came before the element the top of the stack, as this would represent the "i"
        in the sequence i < j < k and nums[i] < nums[k] < nums[j]
        
        for example:
        [3,1,4,2]
        
        keeping the stack in monotonic decreasing order
        3 
        3 1
        4 is now greater than 1, 4 is also greater than 3, so we pop 3 and 1 and push 4
        
        However, we also want to track the minimum we've found so far, otherwise, we wouldn't know when the 
        beginning of the ijk sequence, in this case, 1 would be the min.
        
        so going back
        we push a tuple instead, (3, 3), where the min so far is 3
        now push (1, 1), where the min so far is now 1 (based on min(stack[-1], cur element))
        now we get to 4, we first get the min element (min(Stack[-1], cur element)), which is 1
        
        however because we need to keep it monotonic decreasing, pop out of 3 and 1 and then push (4, 1)
        
        we then see that 2 < 4, but greater than our min element of 1, so we return true here since 
        1 < 4, and 2 < 4, but 2 > 1
        
        as long as we find a sequence where stack[-1] > nums[i], and nums[i] > min element this is valid
        
        """
        stack = []
        previousMin = nums[0]
        for i in range(1, len(nums)):
            # pop out to get strictly decreasing order
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
            # and then check to see if the i j k pattern is valid here (current element > min at the top of the stack, but current element less than the top of the stack)
            if stack and nums[i] > stack[-1][1] and stack[-1][0] > nums[i]:
                return True
            # if not, we store the min number that was found before i (previousMin), then update the value of previousMin
            stack.append((nums[i], previousMin))
            previousMin = min(nums[i], previousMin)

   
        return False
        