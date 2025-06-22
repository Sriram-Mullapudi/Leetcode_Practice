from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  # empty prefix
        
        res = 0
        prefix = 0
        
        for num in nums:
            # Count how many nums so far have nums[i] % modulo == k
            if num % modulo == k:
                prefix += 1
            
            # We want: (prefix - target) % modulo == 0 → target = (prefix - k) % modulo
            target = (prefix - k) % modulo
            res += count[target]
            count[prefix % modulo] += 1
        
        return res
