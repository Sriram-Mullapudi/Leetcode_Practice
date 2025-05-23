from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = sum(nums)
        deltas = [(x ^ k) - x for x in nums]
        
        # Select deltas where XORing increases value
        positive_deltas = [d for d in deltas if d > 0]
        gain = sum(positive_deltas)
        
        if len(positive_deltas) % 2 == 0:
            return total + gain
        else:
            # Remove the smallest positive delta or take the largest negative one
            min_extra_loss = float('inf')
            for d in deltas:
                min_extra_loss = min(min_extra_loss, abs(d))
            return total + gain - min_extra_loss
