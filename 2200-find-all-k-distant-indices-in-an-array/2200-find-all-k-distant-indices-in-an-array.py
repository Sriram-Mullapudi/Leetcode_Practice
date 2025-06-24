from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = set()
        for i, num in enumerate(nums):
            if num == key:
                for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                    result.add(j)
        return sorted(result)
