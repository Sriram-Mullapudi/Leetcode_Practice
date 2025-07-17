from collections import defaultdict
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [defaultdict(int) for _ in range(k)]  # dp[mod][r] = max len ending with mod r under total mod = mod
        res = 1

        for num in nums:
            cur_mod = num % k
            for target in range(k):
                need = (target - cur_mod + k) % k
                prev = dp[target][need]
                dp[target][cur_mod] = max(dp[target][cur_mod], prev + 1)
                res = max(res, dp[target][cur_mod])
        
        return res
