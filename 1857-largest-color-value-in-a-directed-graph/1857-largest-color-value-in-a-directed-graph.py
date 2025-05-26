class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        color_count = [[0] * 26 for _ in range(n)]
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                color_count[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                for c in range(26):
                    color_count[neighbor][c] = max(
                        color_count[neighbor][c],
                        color_count[node][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0)
                    )
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            max_color_value = max(max_color_value, max(color_count[node]))

        return max_color_value if visited == n else -1
