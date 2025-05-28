import java.util.*;

class Solution {
    public int[] maxTargetNodes(int[][] edges1, int[][] edges2, int k) {
        int n = edges1.length + 1;
        int m = edges2.length + 1;

        List<List<Integer>> tree1 = new ArrayList<>();
        List<List<Integer>> tree2 = new ArrayList<>();

        for (int i = 0; i < n; i++) tree1.add(new ArrayList<>());
        for (int i = 0; i < m; i++) tree2.add(new ArrayList<>());

        for (int[] e : edges1) {
            tree1.get(e[0]).add(e[1]);
            tree1.get(e[1]).add(e[0]);
        }

        for (int[] e : edges2) {
            tree2.get(e[0]).add(e[1]);
            tree2.get(e[1]).add(e[0]);
        }

        // Precompute reach counts for tree2 up to depth (k-1)
        int[] tree2Reach = new int[m];
        for (int i = 0; i < m; i++) {
            tree2Reach[i] = bfs(tree2, i, k - 1);
        }

        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            int cnt1 = bfs(tree1, i, k);
            int maxTotal = 0;
            for (int j = 0; j < m; j++) {
                maxTotal = Math.max(maxTotal, cnt1 + tree2Reach[j]);
            }
            res[i] = maxTotal;
        }

        return res;
    }

    private int bfs(List<List<Integer>> tree, int start, int maxDepth) {
        if (maxDepth < 0) return 0;

        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[tree.size()];
        q.add(new int[]{start, 0});
        visited[start] = true;

        int count = 0;
        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int node = curr[0], depth = curr[1];
            count++;

            if (depth == maxDepth) continue;

            for (int nei : tree.get(node)) {
                if (!visited[nei]) {
                    visited[nei] = true;
                    q.add(new int[]{nei, depth + 1});
                }
            }
        }
        return count;
    }
}
