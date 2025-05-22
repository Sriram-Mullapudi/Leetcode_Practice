from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # If any value is less than k, impossible
        if any(x < k for x in nums):
            return -1

        # Count unique values strictly greater than k
        unique_above_k = set(x for x in nums if x > k)
        return len(unique_above_k)
