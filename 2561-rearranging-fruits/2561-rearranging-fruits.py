from collections import Counter

class Solution:
    def minCost(self, basket1, basket2):
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        total = freq1 + freq2

        # 1. Check feasibility
        for v in total.values():
            if v % 2: 
                return -1

        # 2. Target (half count)
        target = {k: v // 2 for k, v in total.items()}

        # 3. Excess fruits
        excess1, excess2 = [], []
        for k in total:
            if freq1[k] > target[k]:
                excess1.extend([k] * (freq1[k] - target[k]))
            if freq2[k] > target[k]:
                excess2.extend([k] * (freq2[k] - target[k]))

        # Sort excess
        excess1.sort()
        excess2.sort(reverse=True)

        # 4. Global min fruit
        globalMin = min(total.keys())

        # 5. Calculate cost
        total_cost = 0
        for a, b in zip(excess1, excess2):
            total_cost += min(min(a, b), 2 * globalMin)

        return total_cost
