class Solution:
    def smallestSubarrays(self, nums):
        n = len(nums)
        last = [-1] * 30   # track last occurrence of each bit
        ans = [0] * n

        for i in range(n-1, -1, -1):
            # update last positions for bits in nums[i]
            for b in range(30):
                if nums[i] & (1 << b):
                    last[b] = i

            # farthest index we must include
            farthest = i
            for b in range(30):
                if last[b] != -1:
                    farthest = max(farthest, last[b])

            ans[i] = farthest - i + 1

        return ans
