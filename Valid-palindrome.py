# Runtime: 136ms ; Memory: 15.2MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return "true"
        else:
            s = s.lower()
            new_s = ''.join(c for c in s if ord(c) in range(48,58) or ord(c) in range(97,123))
            if new_s == new_s[::-1]:
                return True
            else:
                return False
            