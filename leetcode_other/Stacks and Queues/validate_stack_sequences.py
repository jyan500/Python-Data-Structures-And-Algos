"""
https://leetcode.com/problems/validate-stack-sequences/
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        My original thoughts:
        We push, continually check if the last item in PUSH (top of the stack) is the first item in POPPED,
        otherwise continue to push. If the top is equal to the last item, pop and append to our res
        
        if our res == popped, that means this was a possible sequence
        
        A cleaner way of thinking about the problem from leetcode discuss:
        https://leetcode.com/problems/validate-stack-sequences/discuss/197667/JavaPython-3-straight-forward-stack-solution.
        1) Keep pushing pushed elements into stack if the top element on the stack is different from the current one of popped;
        2) Keep popping out of the top element from stack if it is same as the current one of popped;
        3) Check if the stack is empty after loop
        
        O(N) time O(N) Space
        """
#         i = 1
#         j = 0
#         cur = [pushed[0]]
#         res = []
#         while (j < len(popped)):
#             if len(cur) > 0:
#                 top = cur[-1]
#                 if popped[j] == top:
#                     res.append(cur.pop(-1))
#                     j += 1
#                 elif i < len(pushed):
#                     cur.append(pushed[i])
#                     i += 1
#                 else:
#                     break
#             else:
#                 cur.append(pushed[i])
#                 i += 1

#         return res == popped

        # re-did it using the leetcode discuss approach
        res = []
        j = 0
        for i in range(len(pushed)):
            res.append(pushed[i])
            # if the element we just pushed is the same as the current element of 
            # the popped list, continually pop until it's not the same
            while (len(res) > 0 and popped[j] == res[-1]):
                res.pop()
                j += 1
        return len(res) == 0