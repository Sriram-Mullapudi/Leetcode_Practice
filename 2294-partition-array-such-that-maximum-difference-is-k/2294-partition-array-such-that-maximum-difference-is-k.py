class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i = 0

        while i < len(nums):
            start = nums[i]
            count += 1
            while i < len(nums) and nums[i] - start <= k:
                i += 1
                
        return count
