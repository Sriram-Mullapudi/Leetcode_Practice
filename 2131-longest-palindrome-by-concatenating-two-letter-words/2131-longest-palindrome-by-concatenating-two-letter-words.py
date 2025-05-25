class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        used_middle = False

        for word in list(count.keys()):
            rev = word[::-1]
            if word == rev:
                pairs = count[word] // 2
                length += pairs * 4
                count[word] -= pairs * 2
                if count[word] > 0 and not used_middle:
                    length += 2
                    used_middle = True
            elif word < rev:
                pair_count = min(count[word], count[rev])
                length += pair_count * 4
                count[word] -= pair_count
                count[rev] -= pair_count

        return length
