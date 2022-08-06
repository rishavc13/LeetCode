# Find value of a variable after performing operations
# Runtime : 78 ms ; Memory : 13.9 MB

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        op = 0
        for each in operations:
            if "+" in each:
                op += 1
            else:
                op -= 1
        return op