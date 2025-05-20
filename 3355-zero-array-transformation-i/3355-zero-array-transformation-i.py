class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        count = [0] * (n + 1)  # Difference array for range updates

        # Build the difference array
        for l, r in queries:
            count[l] += 1
            if r + 1 < n:
                count[r + 1] -= 1

        # Convert to prefix sum to get final count of how many times each index is covered
        for i in range(1, n):
            count[i] += count[i - 1]

        # Check if each element in nums can be reduced to 0
        for i in range(n):
            if nums[i] > count[i]:
                return False

        return True
