class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        prev_group = groups[0]

        for i in range(1, len(words)):
            if groups[i] != prev_group:
                res.append(words[i])
                prev_group = groups[i]

        return res
