class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        freq = Counter(s)        
        t = []                  
        res = []                 
        min_char = 'a'

        for c in s:
            t.append(c)
            freq[c] -= 1

            # Advance min_char to the smallest character still remaining in s
            while min_char <= 'z' and freq[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # Pop from `t` while top is <= smallest remaining in `s`
            while t and t[-1] <= min_char:
                res.append(t.pop())

        return ''.join(res)
