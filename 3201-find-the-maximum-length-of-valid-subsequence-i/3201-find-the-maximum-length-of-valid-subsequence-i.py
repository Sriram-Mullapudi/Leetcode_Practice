class Solution:
    def maximumLength(self, nums):
        odd_count = sum(1 for x in nums if x % 2 == 1)
        even_count = len(nums) - odd_count

        # Build alternating subsequence
        prev = -1
        alt_len = 0
        for num in nums:
            if prev == -1:
                alt_len += 1
                prev = num % 2
            elif (prev + num) % 2 == 1:
                alt_len += 1
                prev = num % 2

        return max(odd_count, even_count, alt_len)
