class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        https://leetcode.com/problems/crawler-log-folder/
        
        in logs, you always start at the main folder (denoted as "+")
        then the logs show a series of operations that advance into a different folder
        or stays at the current
        figure out how the minimum operations needed to get back to the main folder
        after all the operations are complete

        example: ["d1/","d2/","../","d21/","./"]
        starts at the main folder +

            d1/ (moves to the d1 folder)
                d2/ (moves to d2)
            d1/ (goes back to d1)
                d21/ (goes to d21)
                (remains in the same folder)

        so you can see here that we're two levels deep, so we need
        to perform the "../" operation twice to get back to the main folder

        in order to show where we started and how much progress we've made inside the folder,
        we can use a stack

        [] initially we will start in the main folder, which is the empty stack
        ["d1"] we are now at d1
        ["d1", "d2"] we are now at d2
        ["d1"] we go back to d1
        ["d1", "d21"] we go to d21
        we stay there again with the "./" operation
        therefore, the length of the stack is actually the amount of operations
        needed to get back to an empty stack (which is the main folder) 
        """
        stack = []
        for i in range(len(logs)):
            if len(stack) > 0:
                if logs[i] == "../":
                    stack.pop()
                    continue
            if logs[i] == "./":
                continue
            # there is a case where we can go backwards but we're still at the main folder,
            # account for this by not adding this to the stack
            if logs[i] == "../":
                continue
            stack.append(logs[i])
        return len(stack)
        