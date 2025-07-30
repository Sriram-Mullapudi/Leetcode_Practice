class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)  # Step 1: Find the maximum element
        longest = 0
        current = 0
        
        # Step 2: Traverse the array
        for num in nums:
            if num == max_val:
                current += 1
                longest = max(longest, current)
            else:
                current = 0  # reset streak
        
        return longest
