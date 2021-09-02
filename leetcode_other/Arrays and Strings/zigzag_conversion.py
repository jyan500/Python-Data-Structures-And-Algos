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

