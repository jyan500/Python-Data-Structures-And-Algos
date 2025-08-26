class Solution:
    def minLength(self, s: str) -> int:
        """
        use a stack here (instead of sliding window), because in this case:
        removing "AB"/"CD",
        "FCACDB", if you remove the "CD" you get
        "FCAB", this is a good use case of the stack since you can check the top of the stack,
        and then current letter to see if they create a 2 letter string that's either "AB" or "CD",
        and then remove the top of the stack.

        Time: O(N)
        Space: O(N)
        """
        stack = []
        toRemove = set(["AB", "CD"])
        for i in range(len(s)):
            if len(stack) > 0:
                combination = stack[-1] + s[i]
                if combination in toRemove:
                    stack.pop()
                    continue
            stack.append(s[i])
        return len(stack)