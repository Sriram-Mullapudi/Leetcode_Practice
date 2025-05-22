from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # carry over

        # If all digits were 9, we now have [0,0,...,0], so prepend 1
        return [1] + digits
