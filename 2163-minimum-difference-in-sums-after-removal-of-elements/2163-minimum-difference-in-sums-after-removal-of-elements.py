import heapq

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3

        # Step 1: Left to right (max heap) for smallest n sums
        left_sums = [0] * len(nums)
        max_heap = []
        curr_sum = sum(nums[:n])
        for i in range(n):
            heapq.heappush(max_heap, -nums[i])
        left_sums[n - 1] = curr_sum

        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            curr_sum += nums[i]
            curr_sum += heapq.heappop(max_heap)  # remove the largest (negated min)
            left_sums[i] = curr_sum

        # Step 2: Right to left (min heap) for largest n sums
        right_sums = [0] * len(nums)
        min_heap = []
        curr_sum = sum(nums[-n:])
        for i in range(3 * n - 1, 2 * n - 1, -1):
            heapq.heappush(min_heap, nums[i])
        right_sums[2 * n] = curr_sum

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            curr_sum += nums[i]
            curr_sum -= heapq.heappop(min_heap)
            right_sums[i] = curr_sum

        # Step 3: Find minimum difference
        result = float('inf')
        for i in range(n - 1, 2 * n):
            result = min(result, left_sums[i] - right_sums[i + 1])

        return result
