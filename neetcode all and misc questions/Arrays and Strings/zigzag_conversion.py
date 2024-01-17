'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Revisited on 1/17/2024, 
        still O(N^2) time and O(N^2) space

        Store the result into a 2D array when going through the zig zag pattern
        Loop through each row of the 2D array and save to the string result
        
        The dimensions of the 2D array:
        numrows = same as numRows given as the parameter
        
        It seems you may not know what the number of columns is ahead of time, but
        you can allocate a upper bound where the num of columns == len of the string,
        since we're going in a zig zag, we can assume we'll always use less than if
        we only had one row, and the word was just spelled out in a straight line, which
        would require the same number of columns as the length of the string.
        
        P A Y P A L I S H I R I N G = 14 columns = 14 chars which is the upper bound
        
        Iterate through the 2D array column by column (so outer loop is num cols, inner loop is num rows),
        we determine how many times we need to go on the diagonal by calculating numRows % 2,
        so 3 rows equals one element on the diagonal
        4 rows equals two elements on the diagonal
        5 rows equals three elements on the diagonal, etc
        
        At first we iterate starting from 0, 0 and then going down across the rows
        |
        |
        v
        
        Then, we set our boolean goingDiag to True (if we need to iterate diagonals),
        and then set our diagIndex to numRows - 2 (for example, if numRows = 3, this would be 1)
        |   /
        |  /  
        v /
        
        we do this until diagIndex == 0, then we set goingDiag back to False, and then this will
        cause the iteration to go down the rows again for this column at i
        
        |   / |
        |  /  |
        v /   v
        
        this will then set the diagIndex back to numRows - 2 and repeat.
        
        Note that as we do this, we keep a counter that goes through each character in the string
        and we continue until k == len(s), and then stop the iterations
        """
        numCols = len(s)
        # initialize empty string for each cell space
        grid = [["" for i in range(numCols)] for j in range(numRows)]
        x = 0
        y = 0
        # iterate through the grid column by column
        k = 0
        goingDiag = False
        diagIndex = numRows - 2
        for i in range(numCols):
            if k < len(s):
                if not goingDiag:
                    for j in range(numRows):
                        if k < len(s):
                            grid[j][i] = s[k]
                            k += 1
                        else:
                            break
                    # we don't need to go diagonally for any row count that's less than 3
                    if numRows - 2 > 0:
                        goingDiag = True
                else:
                    # we go diagonally upwards until our diagIndex reaches 0, then
                    # the next iteration will go to the case above and go downwards
                    if k < len(s):
                        grid[diagIndex][i] = s[k]
                        k += 1
                        diagIndex -= 1
                        if diagIndex == 0:
                            goingDiag = False
                            diagIndex = numRows - 2
                    else:
                        break
            else:
                break
        res = []
        for i in range(numRows):
            for j in range(numCols):
                res.append(grid[i][j])
        # this will automatically ignore any of the white space strings that we added that
        # were "empty" cells in our grid
        return "".join(res)
                
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Concept
        Time complexity: O(N^2) (because of the last few statements where we join each row to create the string)
        Space Complexity: O(N^2) (because we're creating a 2D array)
        
        make 2D array based on numRows
        generate the zigzag structure in our 2D array
            iterate through the string
            set counter, from 0 to numRows - 1, increase counter and add s[i] into each grid value going downwards
            after counter == numRows - 1, decrease counter and add s[i] into each grid value going upwards
        iterate through each row in the 2d array and build out the string
        '''
        if (numRows == 0 or numRows == 1):
            return s
        grid = []
        for i in range(numRows):
            grid.append([])
        down = True
        counter = 0
        for i in range(len(s)):
            if (down):
                grid[counter].append(s[i])
                if (counter == numRows-1):                   
                    counter -= 1
                    ## going diagonally upwards now
                    down = False
                else:           
                    counter += 1
            else:
                grid[counter].append(s[i])
                if (counter == 0):
                    counter += 1
                    ## going downwards now
                    down = True
                else:
                    counter -= 1
        res = ''
        ## build out each row
        for i in range(numRows):
            res += ''.join(grid[i])
        return res
        '''
        [
         ['P', 'A'],
         ['A', 'P', 'L'],
         ['Y', 'I']
        ]
        '''

