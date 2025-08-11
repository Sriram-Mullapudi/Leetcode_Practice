from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        exps = []
        i = 0
        while (1 << i) <= n:
            if (n >> i) & 1:
                exps.append(i)
            i += 1
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)
        ans = []
        for L, R in queries:
            s = pref[R + 1] - pref[L]
            ans.append(pow(2, s, MOD))
        return ans
