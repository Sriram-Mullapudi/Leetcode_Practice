import java.util.*;

public class Solution {
    public int maxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        int n = status.length;
        boolean[] visited = new boolean[n];
        boolean[] hasBox = new boolean[n];
        boolean[] hasKey = new boolean[n];

        Queue<Integer> queue = new LinkedList<>();
        
        for (int box : initialBoxes) {
            hasBox[box] = true;
            if (status[box] == 1) {
                queue.offer(box);
                visited[box] = true;
            }
        }

        int totalCandies = 0;
        
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            totalCandies += candies[curr];
            
            for (int key : keys[curr]) {
                hasKey[key] = true;
                if (hasBox[key] && !visited[key]) {
                    queue.offer(key);
                    visited[key] = true;
                }
            }

            for (int box : containedBoxes[curr]) {
                hasBox[box] = true;
                if ((hasKey[box] || status[box] == 1) && !visited[box]) {
                    queue.offer(box);
                    visited[box] = true;
                }
            }
        }
        
        return totalCandies;
    }
}
