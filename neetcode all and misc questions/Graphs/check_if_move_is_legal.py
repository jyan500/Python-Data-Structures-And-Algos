class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        """
        good line = 3 or more cells, endpoints are one color, everything else is the opposite color
        for a move to be legal, the cell must become an endpoint for at least one good line after changing it
        to color (from the parameter)

        W = White, B = Black

        W B B w, is a good line
        B W W B, is a good line
        B W B is also a good line

        Good line can be on the horizontal, vertical or diagonal axis.

        Algorithm:
        since we know that the cell designated by rMove and cMove MUST be an endpoint,
        that means we can start iterating in one of the 8 directions starting from 
        the coordinates (rMove, cMove). We don't have to worry about
        cases where (rMove, cMove) would result in a good line where (rMove, cMove)
        is in the middle of the good line which would be more complex.

        When iterating in a given direction, as long as we're in bounds, and
        the next cell in that direction is the opposite color, continue iterating.
        If we find a cell of the opposite color, and including this cell
        would result in a total cell count >= 3,  this would be the endpoint, so
        we can return True since we've found at least one good line.

        Time: O(N*8)
        Space: O(1)
        """
        def printMatrix():
            for i in range(len(board)):
                row = ""
                for j in range(len(board[0])):
                    row += board[i][j] + " "
                print(row)
        
        def inBounds(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        
        def isOppositeColor(cell):
            return (cell == "B" and color == "W") or (cell == "W" and color == "B")
        
        def isSameColor(cell):
            return (cell == "W" and color == "W") or (cell == "B" and color == "B")

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        
        for x, y in directions:
            newX = x + rMove
            newY = y + cMove
            cellCount = 1
            while (inBounds(newX, newY) and board[newX][newY] != "."):
                # check if the next cell is the opposite color,
                # if so continue iteration
                if isOppositeColor(board[newX][newY]):
                    newX = newX + x
                    newY = newY + y
                    cellCount += 1
                # if including the following cell count is at least 3,
                # And the next cell is the same color, this would be considered an endpoint,
                # so we can return True
                elif cellCount + 1 >= 3 and isSameColor(board[newX][newY]):
                    return True
                # otherwise, no good line was found, continue
                else:
                    break
                
        return False
                