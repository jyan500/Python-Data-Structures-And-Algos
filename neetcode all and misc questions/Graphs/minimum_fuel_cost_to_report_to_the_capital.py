class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """
        ** Need to Revisit ** 
        Neetcode: https://youtu.be/I3lnDUIzIG4
        Time: O(N)
        Space: O(N)
        
        DFS allows you to traverse all the way to the leaf node first, which makes calculations easier, since
        there's no cycles, we can start at 0 and work our way down first using recursion, and then bubble
        the results back up.
        
        At each recursive call, you return the amount of passengers 
        In a global variable, you'd use this formula to calculate the amount of fuel which gets updated inside the DFS.
        Because this is an undirected graph though, track the previous node in the DFS so we don't accidentally
        re-visit the last node and cause an infinite loop (could also use a visited set I think? but would be extra memory)
        fuel = ceil(number of passengers/number of seats)
        Example:
        roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
        
             0
          4  1  5
         6  3
           2
         
        starting at 0, we would start running DFS
        going down 4
        going to 6, there's no more children, so we return 1 here since there's only one passenger
        back to 4
        there's one passenger, (plus the current passenger itself), for a total of two passengers
        ceil(two passengers/two seats) = 1 fuel
        back to 0, there's two passengers so far, ceil(two passengers/two seats) = 1 fuel, total of 2 fuels so far
        
        at 0, it goes down the 2nd path, all the way down to 2
        at 2 to 3, there's one passenger, 1 fuel needed
        at 3 to 1, there's two passengers, ceil(two passengers/two seats) = 1 fuel
        at 1 to 0, there's 3 passengers now, 3 passengers/two seats = 2 fuel needed (because 2 and 3 can be in one car, but 1 has to be in it's own car since there's not enough seats, so 2 total fuel is needed)
        4 fuel total
        
        down the 3rd path...
        5 to 0 takes 1 fuel
        
        2 + 4 + 1 = 7 fuel total
        """
        adjacency = {}
        n = len(roads)
        for i in range(n+1):
            adjacency[i] = []
        for city1, city2 in roads:
            adjacency[city1].append(city2)
            adjacency[city2].append(city1)
        self.totalFuel = 0
        def dfs(node, prev):    
            passengers = 0
            for neighbor in adjacency[node]:
                # make sure we don't revisit the previous node
                if neighbor != prev:
                    numPassengers = dfs(neighbor, node)
                    self.totalFuel += ceil(numPassengers/seats)
                    passengers += numPassengers
            # the reason the + 1 is necessary is because when we reach the leaf node,
            # we need to account for the fact that the leaf node itself is a passenger, so we increment by one
            return passengers + 1
        dfs(0, None)
        return self.totalFuel
        