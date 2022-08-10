# Solution : Runtime : 46ms ; Memory : 13.9MB

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        op = []
        for row in range(1,numRows+1):
            temp = []
            for j in range(row):
                if j==0 or j==row-1:
                    temp.append(1)
                else:
                    temp.append(op[row-2][j-1] + op[row-2][j])
            op.append(temp)
        return op