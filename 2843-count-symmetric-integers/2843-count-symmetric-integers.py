class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(x: int) -> bool:
            s = str(x)
            if len(s) % 2 != 0:
                return False
            mid = len(s) // 2
            return sum(map(int, s[:mid])) == sum(map(int, s[mid:]))

        count = 0
        for num in range(low, high + 1):
            if is_symmetric(num):
                count += 1
        return count
