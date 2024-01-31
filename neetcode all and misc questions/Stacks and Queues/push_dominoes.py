class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Neetcode's Queue Solution:
        O(N) Time
        O(N) Space
        https://leetcode.com/problems/push-dominoes/
        https://www.youtube.com/watch?v=evUFsOb_iLY&t=1058s&ab_channel=NeetCode
        The approach using a queue does a simulation one pass at a time,
        where we do an initial pass to get all left and right fall dominoes,
        and then as we pop from the queue,
        we check whether the domino immediately to the left or right is upright,
        and if so, if we would set that domino to either L/R, and then append
        that to the queue, and then repeat.
        
        For example:
        R..L
        We'd first get (R, 0) and (L, 3) onto the queue.
        
        We pop out (R, 0), we set index 1 to R and then append (R, 1) onto the queue
        We pop out (L, 3), we set index 2 to L and then append (L, 2) onto the queue
        
        At (R, 1), we realize that we can't knock over any more dominoes since index 2 is
        no longer upright, same with (L, 2)
        
        There are some edge cases, where if we have
        R.L, 
        we'd have to account that the middle domino cannot be knocked over since it's between
        and L and R
        
        If we have an L domino with nothing before it, all dominoes before this L can also be set to L
        
        """
        from collections import deque
        q = deque()
        dominoes = list(dominoes)
        for i in range(len(dominoes)):
            if dominoes[i] != ".":
                q.append((dominoes[i], i))
        
        while (q):
            fallType, index = q.popleft()
            if fallType == "L":
                # if the spot before L is in bounds of the array and
                # it's upright, set it to L
                if index - 1 >= 0 and dominoes[index-1] == ".":
                    dominoes[index-1] = "L"
                    q.append((dominoes[index-1], index-1))
            else:
                if index + 1 < len(dominoes) and dominoes[index+1] == ".":
                    # this is the special case where we have an R.L
                    # in this case, we need to popleft once more such that the 
                    # left domino to the left of . gets popped out, otherwise,
                    # this would cause this . to be turned into L, which is incorrect
                    if index + 2 < len(dominoes) and dominoes[index+2] == "L":
                        q.popleft()
                    else:
                        dominoes[index+1] = "R"
                        q.append((dominoes[index+1], index+1))
        return "".join(dominoes)

        """
	    My first 'hacky' solution using a stack,
	    track the index where the domino falls, as well
	    as whether it's a Left/Right, within a tuple
	    
	    looping through, it essentially evaluates two edge cases,
	    where you have two right fall dominoes,
	    or a right fall domino followed by a left fall domino
	    
	    any left fall dominoes will automatically push all the dominoes 
	    before it over to the left
	    
	    and remaining right fall dominoes that haven't been evaluated and
	    remained on the stack will fall to the right
	    """ 
	    """
        stack = []
        dominoes = list(dominoes)
        res = dominoes.copy()
        for i in range(len(dominoes)):
            if dominoes[i] == "L" or dominoes[i] == "R":
                if len(stack) > 0:
                    # intercepting dominoes
                    fallType, index = stack[-1]
                    # if the previous fall type was Right, and this was another right domino
                    # we set all the upright dominoes to R, and then we still append
                    # the current right fall domino because there may be a future left fall
                    # domino we need to account for
                    if fallType == "R" and dominoes[i] == "R":
                        for j in range(i, index-1, -1):
                            if res[j] == ".":
                                res[j] = "R"
                        stack.pop()
                        stack.append((dominoes[i], i))
                        continue
                    if fallType == "R" and dominoes[i] == "L":
                        stack.pop()
                        # if there are an even amount of spaces between
                        # the right and left fall, we set an equal amount of Rights and Lefts
                        # only for upright dominoes (dominoes[i] == ".")
                        amt = (i - index - 1) // 2
                        for j in range(index+1, index+amt+1):
                            if res[j] == ".":
                                res[j] = "R"
                            else:
                                break
                        for j in range(i-1,i-amt-1,-1):
                            if res[j] == ".":
                                res[j] = "L"
                            else:
                                break
                        continue
                        
                # if we encounter a Left fall, that means everything before this index
                # that are upright dominoes
                # can be set to L assuming we didn't run into a right fall earlier
                if dominoes[i] == "L":
                    for j in range(i-1, -1, -1):
                        if res[j] == ".":
                            res[j] = "L"
                        else:
                            break
                    continue
                        
                stack.append((dominoes[i], i))
        # if there are any remaining right fall dominoes we haven't accounted for
        # (since we've evaluated all pairs of Right and Left dominoes, as well as Left Dominoes)
        # set all the remaining upright dominoes to right
        for fallType, index in stack:
            if fallType == "R":
                for i in range(index+1, len(res)):
                    if res[i] == ".":
                        res[i] = "R"
                    else:
                        break
        return "".join(res)
        """