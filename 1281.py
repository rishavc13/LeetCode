# Subtract the product and sum of digits of a number

# Runtime : 35ms ; Memory : 13.9 MB

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        su = 0
        product = 1
        while n!= 0:
            remainder = n % 10
            su = su + remainder
            product = product * remainder
            n = n//10
        return product - su


# Solution 2 : Space = O(log n)

def subtractProductAndSum(self, n):
        A = map(int, str(n))
        return reduce(operator.mul, A) - sum(A)