# Solution 1: Runtime 280 ms  Memory 15.6 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        nums.append("_")
        while(nums[i] != "_"):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)-1
