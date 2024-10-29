class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        BFS

        Time: O(M*N), where you could potentially visit every cell if there are no snakes and ladders
        Space: O(M), needed for the ranges dict

        Dice roll sends you forward in the board positioning
        add 1, or 2, or 3 ... until 6
        if the board position has a number that's not -1, that will send
        you to that board position listed (i.e 15)
        
        In BFS, you keep track of the position (a number from 1 to len(board) ** 2), and the number of moves in a tuple.
        Then, you apply normal BFS, where the neighbors are just for i in range(0, 6), where you add i + currentPosition + 1
        to get the next position. Then convert the position to the actual board coordinates.

        You keep a visited set to avoid re-visiting previous cells, and then stop the BFS if our current position is len(board) ** 2

        The tricky part of this problem is converting from the position to the actual coords.

        I'm not sure if this is the best way, but kept track of a dict that maps the row indices to the min and max positions that exist 
        within each row. i.e for a 6 x 6 board
        
        36 35 34 33 32 31
        25 26 27 28 29 30
        24 23 22 21 20 19
        13 14 15 16 17 18 
        12 11 10 9  8  7
        1  2  3  4  5  6

        5 maps to [1, 6]
        4 maps to [7, 12]
        3 maps to [13, 18]
        2 maps to [19, 24]
        1 maps to [25, 30]
        0 maps to [31, 36]

        the logic is that given the position and len(board), the equation below gives you the row index: 
        len(board) - 1 - ((position-1) // len(board)) 

        the reason why this works is because any number between a given range n will always map back to a specific number
        when you divide by n. You also need to subtract 1 from the position first, otherwise this would give you the wrong number,
        where the max for each position would get wrapped 'up' one row, i.e in a 6x6, 6 belows on row 5 and not row 4

        for example, for numbers 1 to 6. If you subtract 1 from the position first, then do integer division by 6, you'll always get 0, 0/6 = 0, 1/6 = 0, ... 5/6 = 0
        you then need to take len(board) - 1 - this number to get the actual row index, in this case, 5

        To find the column, you need to see whether the current row is odd or even, and also check to see if the total number
        of columns is odd or even

        get the minimum of the range based on the row index within the dict, i.e the value for ranges[5] would be [1,6],
        and the min would therefore be ranges[5][0]

        If the current row is odd, we would subtract the current position from the row min IF the TOTAL number of columns is even,
        otherwise, we would need to do len(board) - (current position - row min) - 1

        If the current row is even, we would do len(board) - (current position - row min) - 1 if total number of columns is even,
        otherwise do current position - row min

        For example:
        Given the position 19, this maps to row 2. Because the board is 6 x 6, this means that 
        on row 1, the values should be in descending order. 
        Therefore, we would do position - rowmin, which is 19 - 19 = 0
        And then do len(Board) - this number - 1, which gives us 6 - 0 - 1 = 5

        This is correct since 19 is in column 5, giving us the indices row 2, column 5

        """
        from collections import deque
        ranges = {}
        i = 1
        n = len(board)
        k = n - 1
        # map the ranges of the board based on the indices
        while (i <= n**2):
            ranges[k] = [i, i + n - 1]
            i = i + n
            k -= 1
          
        def convertPosToCoord(position):
            """
            n = 6
            6, (n-1, n-1)
            12, (n-2, 0)
            18, (n-3, n-3)
            24 (n-4, 0)
            30, (n-5, n-5)
            36 (n-6, 0)
            
            29//6 = 4 (n - 1 - 4, gives us 1)
            Integer division n-1-(position/n) gives us 1, which tells us the row
            coordinate. 
  
            """
            # divisible by n, this is the at end of one of the rows
            row = n - 1 - ((position-1) // n)
            rowMin = ranges[row][0]
            column = 0
            # even numbered row means numbers are descending
            # take the min for that row based on ranges, and subtract
            # position from rowMin, and then subtract from n - 1
            # since the numbers are descending
            # note that in boards with odd numbered rows and cols, this logic
            # is reversed, where odd numbered rows are descending instead
            if row % 2 == 0:
                column = n - (position - rowMin) - 1 if n % 2 == 0 else position - rowMin 
            else:
                column = position - rowMin if n % 2 == 0 else n - (position - rowMin) - 1
            return [row, column]
      
        q = deque() # [(square, moves)]
        q.append([1, 0])
        visit = set()
        minMoves = float("inf")
        while (q):
            square, numMoves = q.popleft()
            if (square == n ** 2):
                minMoves = min(minMoves, numMoves)
                continue
            if (square in visit):
                continue
            visit.add(square)
            for k in range(6):
                nextSquare = square + k + 1
                if (nextSquare <= n**2):
                    i, j = convertPosToCoord(nextSquare)
                    if board[i][j] == -1:
                        q.append((nextSquare, numMoves + 1))
                    else:
                        # this is either a snake or ladder
                        q.append((board[i][j], numMoves + 1))
        return minMoves if minMoves != float("inf") else -1
                
        
                
            
                
                