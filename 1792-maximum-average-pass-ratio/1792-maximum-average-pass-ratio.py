import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        # max-heap using negative keys
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t
        return total / len(classes)
