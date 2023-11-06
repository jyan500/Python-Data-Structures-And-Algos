"""
Time Complexity: 
O(N^2)
Space:
O(N^2)

Key Concepts:
To calculate the next level of pascal's triangle:
1) initially add 1
2) Use 2 pointers to iterate through the previous row of pascal's triangle that we added to sum
up the two numbers above
3) Add 1 to complete this level and add to our result

    1 4 6 4 1

j = 0
k = 1

cur = [1]

1 + 4 = 5

cur = [1, 5]

Iterate, j = 1 k = 2

4 + 6 = 10

cur = [1, 5, 10]

Iterate, j = 2 k = 3

6 + 4 = 10

cur = [1, 5, 10, 10]

Iterate, j = 3 k = 4

4 + 1 = 5

cur = [1, 5, 10, 10, 5]

Finally, append 1

cur = [1, 5, 10, 10, 5, 1]

"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        1 4 6 4 1
      1 5 10 10 5 1
        """
        rows = []
        rows.append([1])
        for i in range(1, numRows):
            if i == 1:
                rows.append([1, 1])
            else:
                cur = [1]
                j = 0
                k = 1
                while (k < len(rows[-1])):
                    cur.append(rows[-1][j]+rows[-1][k])
                    j += 1
                    k += 1
                cur.append(1)
                rows.append(cur)
        return rows
                