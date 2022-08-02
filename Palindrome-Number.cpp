class Solution {
public:
    bool isPalindrome(int x) {
        int rem, flag=1;
        long temp=x, rev=0;
        if(x < 0) {
            flag = 0;
        }
        else {
            while(temp != 0) {
                rev = (rev*10) + (temp%10);
                temp = temp/10;
            }
            if(rev != x) {
                flag = 0;
            }
        }

        return flag;
        
    }
};