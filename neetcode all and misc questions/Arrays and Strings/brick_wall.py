class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        Thoughts:
        The numbers in each 2D array will always add up to the same amount
        For example:
        wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
        
        Between each "brick" is an empty space, we can call that X
            
        If we increment the amount of X's we visit, the max amount of X's will be our answer,
        via reverse thinking, we would've hit the least amount of walls if we maximize the amount of 
        empty space X's that we cross. We just need to figure out the amount of X's that line up
        across each row
        
        We can treat the space between each index as a "half" index, for example:
        wall = [[4,5,1],[2,1,2,5],[1,2,1,2,4]]
        
                0 1 2 3 4 5 6 7 8 9
        4 5 1 = 1 1 1 1 1 1 1 1 1 1 
                ^     ^ ^       ^ ^
        between index 3 and 4 is an empty space, so we denote this as "3.5"
        between 8 and 9 is another empty space, so this is "8.5"
        
        2 1 2 5 = 0 1 2 3 4 5 6 7 8 9
                  1 1 1 1 1 1 1 1 1 1
                  ^ ^ ^ ^ ^ ^       ^
        
        between 1 and 2 is an empty space, "1.5"
        between 2 and 3 is an empty space, "2.5"
        between 3 and 4 is an empty space, "3.5",
        between 4 and 5 is an empty space, "4.5"
        
        1 2 1 2 4 = 0 1 2 3 4 5 6 7 8 9
                    1 1 1 1 1 1 1 1 1 1
        
        between 0 and 1 is an empty space, .5
        between 2 and 3 is an empty space, 2.5
        between 3 and 4 is an empty space, 3.5
        between 4 and 5 is an empty space, 4.5
        
        
        We then store all the empty space indices in a dict, and then count the 
        greatest amount of empty spaces. 
        
        We can then subtract this amount off of the amount of rows to get our final answer,
        which will be the minimum amount of bricks crossed 
        (min amount of bricks crossed = amt of rows - max amount of empty spaces)

        Time Complexity: O(M*N), where M is the amount of rows and N is the amount of bricks inside each row
        Space: O(N)

        """        
        lookup = dict()
        currentMax = float("-inf")
        for i in range(len(wall)):
            k = 0
            for j in range(len(wall[i])):
                element = wall[i][j]
                k += element
                if j != len(wall[i]) - 1:
                    if k + .5 not in lookup:
                        lookup[k + .5] = 1
                    else:
                        lookup[k + .5] += 1
                    currentMax = max(lookup[k+.5], currentMax)
        return len(wall) - currentMax if currentMax != float("-inf") else len(wall)
        
        
                
                
                
                
                
        