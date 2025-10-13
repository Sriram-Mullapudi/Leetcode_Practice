from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def sig(w: str) -> tuple:
            cnt = [0]*26
            for ch in w:
                cnt[ord(ch) - 97] += 1
            return tuple(cnt)

        res = []
        prev = None
        for w in words:
            s = sig(w)
            if s != prev:
                res.append(w)
                prev = s
        return res
