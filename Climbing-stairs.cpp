// Brute Force Recursion : Time Limit Exceeded

class Solution {
public:
    int climbStairs(int n) {
        int op;
        if(n==0) {
            return 1;
        }
        else if(n==-1) {
            return 0;
        }
        op = climbStairs(n-1) + climbStairs(n-2);
        return op;
    }
};

// Solution 2: Runtime = 0 ms; Memory = 6 MB

class Solution {
public:
    int climbStairs(int n) {
        int a=1, b=2, t;
        if(n==1) {
            return a;
        }
        else if(n==2) {
            return b;
        }
        else {
            while(n-2 > 0) {
                t = a + b;
                a = b;
                b = t;
                n = n - 1;
            }
            return t;
        }
    }
};