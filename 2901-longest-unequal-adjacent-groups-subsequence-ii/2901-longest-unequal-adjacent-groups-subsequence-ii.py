from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n  # dp[i] = longest subsequence ending at i
        prev = [-1] * n  # for reconstructing path

        # Helper: Check if two strings have hamming distance of 1
        def is_hamming_one(a: str, b: str) -> bool:
            if len(a) != len(b):
                return False
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        # Try all i < j, if valid transition from i to j, update dp[j]
        for j in range(n):
            for i in range(j):
                if groups[i] != groups[j] and is_hamming_one(words[i], words[j]):
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1
                        prev[j] = i

        # Find max length and end index
        max_len = max(dp)
        idx = dp.index(max_len)

        # Reconstruct the subsequence
        result = []
        while idx != -1:
            result.append(words[idx])
            idx = prev[idx]
        return result[::-1]
