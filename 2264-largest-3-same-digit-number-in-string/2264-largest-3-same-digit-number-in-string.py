class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                s = num[i:i+3]
                if s > best:      # lexicographic compare is fine for length-3 digits
                    best = s
        return best
