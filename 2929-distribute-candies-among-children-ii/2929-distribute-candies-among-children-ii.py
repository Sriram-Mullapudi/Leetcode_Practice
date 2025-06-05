class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(a):
            return (a + 2) * (a + 1) // 2 if a >= 0 else 0
        
        total = comb(n)
        over1 = 3 * comb(n - (limit + 1))
        over2 = 3 * comb(n - 2 * (limit + 1))
        over3 = comb(n - 3 * (limit + 1))
        
        return total - over1 + over2 - over3
