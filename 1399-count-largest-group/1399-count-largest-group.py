from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = Counter()

        for num in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(num))
            count[digit_sum] += 1

        max_size = max(count.values())
        return sum(1 for v in count.values() if v == max_size)
