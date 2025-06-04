class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        self.maxWord = ""
        n = len(word)

        def dfs(index, splitsLeft, parts):
            # Base case: only one part left to split, take the rest
            if splitsLeft == 1:
                if index < n:
                    parts.append(word[index:])
                    for p in parts:
                        self.maxWord = max(self.maxWord, p)
                    parts.pop()
                return

            # Try next cut from index+1 to where there's enough remaining characters
            for i in range(index + 1, n - splitsLeft + 2):  # +1 for inclusive slice
                parts.append(word[index:i])
                dfs(i, splitsLeft - 1, parts)
                parts.pop()

        dfs(0, numFriends, [])
        return self.maxWord
