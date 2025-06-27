from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def is_valid(t):
            # Check if t * k is subsequence of s
            t_k = t * k
            i = 0
            for c in s:
                if c == t_k[i]:
                    i += 1
                    if i == len(t_k):
                        return True
            return False

        counter = Counter(s)
        chars = sorted([c for c in counter if counter[c] >= k], reverse=True)
        if not chars:
            return ""

        # BFS
        queue = deque([""])
        best = ""
        
        while queue:
            cur = queue.popleft()
            for c in chars:
                new_candidate = cur + c
                # BFS ensures we try shorter strings first
                if is_valid(new_candidate):
                    if (len(new_candidate) > len(best)) or \
                       (len(new_candidate) == len(best) and new_candidate > best):
                        best = new_candidate
                    queue.append(new_candidate)
        return best
