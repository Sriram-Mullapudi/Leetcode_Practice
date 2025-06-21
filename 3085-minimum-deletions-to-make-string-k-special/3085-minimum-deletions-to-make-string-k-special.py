from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        min_del = float('inf')
        
        for target in freq:
            deletions = 0
            for f in freq:
                if f < target:
                    deletions += f  # delete entire group
                elif f > target + k:
                    deletions += f - (target + k)
            min_del = min(min_del, deletions)
        
        return min_del
