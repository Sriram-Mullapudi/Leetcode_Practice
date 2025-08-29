class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Count odds and evens in [1..n] and [1..m]
        on, en = (n + 1) // 2, n // 2
        om, em = (m + 1) // 2, m // 2
        # Alice wins when x+y is odd
        return on * em + en * om
