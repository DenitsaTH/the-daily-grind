'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.'''


class Solution:
    def generate(self, numRows):

        res = []

        for r in range(numRows):
            current_row = []

            for j in range(r + 1):
                if j == 0 or j == r:
                    current_row.append(1)
                else:
                    x, y = res[r - 1][j - 1], res[r - 1][j]
                    current_row.append(x + y)

            res.append(current_row)

        return res
