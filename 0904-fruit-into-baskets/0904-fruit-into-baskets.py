from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        count = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            # shrink window if more than 2 distinct fruits
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            # update max length
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
