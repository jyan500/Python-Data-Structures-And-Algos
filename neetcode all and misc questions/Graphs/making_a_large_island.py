class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        1 0 1 1
        1 0 1 0
        1 0 1 1
        0 0 0 0

        in this example, you could change (1, 0) to be 1, to get
        a total area of 9, or you could change
        (1, 3) to 1, and get a total area of 6, which would be the largest island here

        Brute Force Solution:
        Store the indices for each connected island in a hashmap

        Store a default max by getting max(len(array of indices)) within the hashmap

        Then, figure out if there's at least one cell with a value of 0 across two islands
        by iterating across each 0, and then choosing all 4 directions, and then seeing
        if there's a cell with a value of 1. If so, we can mark this island as seen,
        and add to the total area seen so far, and then take the max of this. We also need to 
        keep a visited set within this to make sure we don't double count an island's area of another neighboring cell.

        Time: O(N^2 * number of islands)

        Slightly Optimized Solution:
        Instead of storing all the indices of each island, we just mark them with a unique ID.
        And then our hashmap would map the unique ID to the total cells found for that unique ID (which would
        be calculated as we run DFS on the island)
        After that, in the second phase where we look at 0's and see if a cell is in the island,
        we can look in all four directions, and check if the cell's value is in our hashmap, since it would have
        a unique counter value if it was in an island, then we can just get the islands' area and add it to the total
        like in the original brute force solution.

        We save the time of needing to track down whether that set of indices exists in the island or not and instead,
        just do a simple ID comparison to check if it exists.

        Time: O(N^2)

        """


        N = len(grid)
        globalVisited = set()
        islands = {}
        # since islands can only have 0 or 1, we just pick 2 as the starting counter for unique island IDs
        counter = 2
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        maxArea = 0

        def inBounds(i,j):
            return 0 <= i < N and 0 <= j < N
        
        def dfs(i,j):
            totalArea = 0
            for x,y in directions:
                newX = x + i
                newY = y + j
                # by mutating the grid, we know that visited cells will be changed to the counter's value,
                # so we don't need a visited set unlike other problems.
                if inBounds(newX, newY) and grid[newX][newY] == 1:
                    # change this to the counter
                    grid[newX][newY] = counter
                    totalArea += dfs(newX, newY) + 1
            return totalArea

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    grid[i][j] = counter
                    totalArea = 1
                    totalArea += dfs(i,j)
                    islands[counter] = totalArea
                    counter += 1
        # assuming that we make no changes from 0 to 1, we would find the largest island and set the
        # default max
        maxArea = max(islands.values()) if len(islands) > 0 else 0
        for i in range(N):
            for j in range(N):
                # starting at totalArea == 1 assuming we flip i,j to 1
                if grid[i][j] == 0:
                    seenIslands = set()
                    totalArea = 1
                    for x,y in directions:
                        newX = x + i
                        newY = y + j
                        # if the cell next to us is in an island (since it'd have one of the counter values)
                        if inBounds(newX, newY) and grid[newX][newY] >= 2 and grid[newX][newY] not in seenIslands:
                            # mark the island as seen so we don't double count the area if another
                            # neighboring cell is in the same island
                            seenIslands.add(grid[newX][newY])
                            # get the area of this island based of its counter id value
                            totalArea += islands[grid[newX][newY]]
                    maxArea = max(maxArea, totalArea)
        return maxArea
        
        
        # First pass:
        # N = len(grid)
        # globalVisited = set()
        # islands = {}
        # counter = 0
        # directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # maxArea = 0

        # def inBounds(i,j):
        #     return 0 <= i < N and 0 <= j < N
        # def dfs(i,j,visited):
        #     for x, y in directions:
        #         newX = x + i
        #         newY = y + j
        #         if inBounds(newX,newY) and (newX, newY) not in visited and grid[newX][newY] == 1:
        #             visited.add((newX, newY))
        #             globalVisited.add((newX, newY))
        #             dfs(newX,newY, visited)

        # for i in range(N):
        #     for j in range(N):
        #         if grid[i][j] == 1 and (i,j) not in globalVisited:
        #             cells = set([(i,j)])
        #             dfs(i,j, cells)
        #             islands[counter] = cells
        #             counter += 1

        # maxArea = 0
        # # assuming no 0's are changed, we would set the default max result to be the island with the largest
        # # total area
        # for key in islands:
        #     maxArea = max(maxArea, len(islands[key]))
        # for i in range(N):
        #     for j in range(N):
        #         if grid[i][j] == 0:
        #             # check the four directions if a cell is connected to one of the islands
        #             totalArea = 1
        #             seenIslands = set()
        #             for x, y in directions:
        #                 newX = x + i
        #                 newY = y + j
        #                 # total area is 1 so far since we're assuming we change i,j to a "1" value,
        #                 # for a total area of 1
        #                 if inBounds(newX, newY) and grid[newX][newY] == 1:
        #                     # find the cell within the lslands
        #                     for key in islands:
        #                         islandSet = islands[key]
        #                         # make sure that if we see a cell within an island twice, we don't
        #                         # double count the total islands' area by keeping track of the seenIslands k
        #                         if (newX, newY) in islandSet and key not in seenIslands:
        #                             totalArea += len(islandSet)
        #                             seenIslands.add(key)
        #             maxArea = max(totalArea, maxArea)
        # return maxArea

