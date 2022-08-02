# Solution 1: Runtime 46ms;  Memory 13.9MB

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        else:
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1


# Solution 2: Runtime 71ms; Memory 13.9MB

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        else:
            n = len(needle)
            op = -1
            for i in range(len(haystack)-len(needle)+1):
                if(haystack[i:i+n] == needle):
                    return i
            return op