# Runtime: 999ms ; Memory: 25.9MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) == len(set(nums))):
            return False
        else:
            return True