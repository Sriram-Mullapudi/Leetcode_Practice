class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        value = 0
        power = 1
        
        # Step 1: Include as many 0s as we want
        zeros = s.count('0')
        count += zeros
        
        # Step 2: Try including 1s from the end (least significant bit)
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if power > k:
                    break  # Adding this bit will overflow k
                value += power
                if value <= k:
                    count += 1
                else:
                    break
                power <<= 1  # Move to next significant bit
            elif s[i] == '0':
                power <<= 1  # 0s don't affect value but shift still matters
                
        return count
