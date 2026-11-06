
import java.util.*;

class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        // Sort logs by time
        Arrays.sort(logs, (a, b) -> a[1] - b[1]);

        int m = queries.length;
        int[][] sortedQueries = new int[m][2];

        for (int i = 0; i < m; i++) {
            sortedQueries[i][0] = queries[i];
            sortedQueries[i][1] = i;
        }

        // Sort queries by time
        Arrays.sort(sortedQueries, (a, b) -> a[0] - b[0]);

        int[] count = new int[n + 1];
        int[] ans = new int[m];

        int left = 0, right = 0;
        int activeServers = 0;

        for (int[] query : sortedQueries) {
            int time = query[0];
            int index = query[1];

            // Add requests with time <= query time
            while (right < logs.length && logs[right][1] <= time) {
                int server = logs[right][0];

                if (count[server] == 0) {
                    activeServers++;
                }

                count[server]++;
                right++;
            }

            // Remove requests before query time - x
            while (left < right && logs[left][1] < time - x) {
                int server = logs[left][0];

                count[server]--;

                if (count[server] == 0) {
                    activeServers--;
                }

                left++;
            }

            ans[index] = n - activeServers;
        }

        return ans;
    }
}
