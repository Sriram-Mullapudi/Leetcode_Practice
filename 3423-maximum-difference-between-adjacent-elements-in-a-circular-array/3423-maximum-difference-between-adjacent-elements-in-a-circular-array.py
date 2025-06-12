class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxDiff = 0

        for i in range(n):
            next_i = (i + 1) % n  # circular neighbor
            diff = abs(nums[i] - nums[next_i])
            maxDiff = max(maxDiff, diff)

        return maxDiff
