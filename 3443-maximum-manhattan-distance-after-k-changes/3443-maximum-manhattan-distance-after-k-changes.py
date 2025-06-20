class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # Direction vectors
        dx = {'N': 0, 'S': 0, 'E': 1, 'W': -1}
        dy = {'N': 1, 'S': -1, 'E': 0, 'W': 0}
        directions = ['N', 'S', 'E', 'W']
        
        n = len(s)
        max_dist = 0

        from heapq import heappush, heappop

        # We use a max heap to always explore the path that gives us greatest distance
        # State: (-distance, index, x, y, k_left)
        heap = [(-0, 0, 0, 0, k)]
        visited = dict()  # (index, x, y): k_left

        while heap:
            neg_dist, i, x, y, k_left = heappop(heap)
            dist = -neg_dist
            max_dist = max(max_dist, dist)

            if i == n:
                continue

            key = (i, x, y)
            if key in visited and visited[key] >= k_left:
                continue
            visited[key] = k_left

            # 1. Use current character
            dx0 = dx[s[i]]
            dy0 = dy[s[i]]
            heappush(heap, (-(abs(x + dx0) + abs(y + dy0)), i + 1, x + dx0, y + dy0, k_left))

            # 2. Try all 3 possible changes (not same direction), if k_left > 0
            if k_left > 0:
                for d in directions:
                    if d == s[i]:
                        continue
                    dx1 = dx[d]
                    dy1 = dy[d]
                    heappush(heap, (-(abs(x + dx1) + abs(y + dy1)), i + 1, x + dx1, y + dy1, k_left - 1))

        return max_dist
