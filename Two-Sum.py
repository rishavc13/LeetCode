# Solution 1: Runtime = 870 ms  Memory Usage = 14.9 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op = []
        for i in range(0, len(nums)):
            if((target-nums[i]) in nums[i+1:]):
                op.append(i)
                op.append(nums[i+1:].index(target-nums[i])+(i+1))
                break
        return op


# Solution 2: Runtime = 64 ms  Memory Usage = 15.4 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]