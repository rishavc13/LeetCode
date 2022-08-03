// Solution 1: Time=9ms; Memory=6.6MB

class Solution {
public:
    int lengthOfLastWord(string s) {
        int tail = s.length() - 1;
        int val = 0;
        while(s[tail] == ' ') {
            tail--;
        }
        while(tail >=0 && s[tail]!=' ') {
            val++;
            tail--;
        }
        return val;
    }
};