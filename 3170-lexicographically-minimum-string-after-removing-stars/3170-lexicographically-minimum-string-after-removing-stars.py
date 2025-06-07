class Solution:
    def clearStars(self, s: str) -> str:
        from collections import defaultdict, deque

        count = defaultdict(deque)
        stack = []

        for i, c in enumerate(s):
            if c != '*':
                stack.append(c)
                count[c].append(len(stack) - 1)
            else:
                # Remove smallest character from the stack
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if count[ch]:
                        idx = count[ch].pop()
                        stack[idx] = None  # Mark as removed
                        break

        return ''.join(c for c in stack if c)
