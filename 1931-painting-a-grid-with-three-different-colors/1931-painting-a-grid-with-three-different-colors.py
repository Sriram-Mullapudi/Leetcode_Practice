class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        colors = [0, 1, 2]

        # Step 1: Generate all valid vertical colorings (no adjacent same colors in column)
        def generate_col_states(pos=0, prev=-1, state=()):
            if pos == m:
                col_states.append(state)
                return
            for c in colors:
                if c != prev:
                    generate_col_states(pos + 1, c, state + (c,))

        col_states = []
        generate_col_states()

        # Step 2: Build valid transitions between columns (no same color at same row)
        transitions = {state: [] for state in col_states}
        for a in col_states:
            for b in col_states:
                if all(x != y for x, y in zip(a, b)):
                    transitions[a].append(b)

        # Step 3: Initialize DP for first column
        dp = {state: 1 for state in col_states}

        # Step 4: DP for each column
        for _ in range(n - 1):
            new_dp = {state: 0 for state in col_states}
            for curr in col_states:
                for prev in transitions[curr]:
                    new_dp[curr] = (new_dp[curr] + dp[prev]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
