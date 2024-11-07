"""
https://leetcode.com/problems/design-browser-history/
"""
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        # remove anything past current (the urls that were reachable by 'forwards' arrow)
        self.history = self.history[:self.current+1]
        # append and then set the self.current pointer to be the len(self.history)-1
        self.history.append(url)
        self.current = len(self.history)-1

    def back(self, steps: int) -> str:
        if (self.current - steps < 0):
            self.current = 0
        else:
            self.current -= steps
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        if (self.current + steps > len(self.history)-1):
            self.current = len(self.history)-1
        else:
            self.current += steps
        return self.history[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)