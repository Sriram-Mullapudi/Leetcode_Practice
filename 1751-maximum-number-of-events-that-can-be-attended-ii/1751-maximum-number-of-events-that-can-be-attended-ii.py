from bisect import bisect_right

class Solution:
    def maxValue(self, events, k):
        # Step 1: Sort events by end day
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Step 2: Extract start times to binary search
        end_times = [e[1] for e in events]
        
        # Step 3: DP array: dp[i][j] = max value using first i events and j picks
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j == 0:
                return 0

            # Option 1: Skip current
            option1 = dp(i - 1, j)

            # Option 2: Take current
            # Find the last non-overlapping event
            start = events[i][0]
            value = events[i][2]
            prev = bisect_right(end_times, start - 1) - 1
            option2 = dp(prev, j - 1) + value

            return max(option1, option2)

        return dp(n - 1, k)
