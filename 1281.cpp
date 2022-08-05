// Subtract the product and sum of digits of a number

// Runtime : 0ms ; Memory : 6MB

class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1, sum = 0, remainder = 0;
        while(n!=0) {
            remainder = n % 10;
            product = product * remainder;
            sum = sum + remainder;
            n = n / 10;
        }
        return (product-sum);
    }
};