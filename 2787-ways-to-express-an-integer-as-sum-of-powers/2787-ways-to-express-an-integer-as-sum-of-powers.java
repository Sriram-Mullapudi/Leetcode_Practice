class Solution {
    private static final int MOD = 1_000_000_007;

    public int numberOfWays(int n, int x) {
        int[] powers = buildPowers(n, x);

        int[] dp = new int[n + 1];
        dp[0] = 1;

        for (int p : powers) {
            for (int s = n; s >= p; s--) {
                dp[s] += dp[s - p];
                if (dp[s] >= MOD) dp[s] -= MOD;
            }
        }
        return dp[n];
    }

    private int[] buildPowers(int n, int x) {
        java.util.ArrayList<Integer> list = new java.util.ArrayList<>();
        for (int base = 1; ; base++) {
            long p = ipow(base, x);
            if (p > n) break;
            list.add((int) p);
        }
        int[] arr = new int[list.size()];
        for (int i = 0; i < arr.length; i++) arr[i] = list.get(i);
        return arr;
    }

    private long ipow(int a, int b) {
        long res = 1, x = a;
        while (b > 0) {
            if ((b & 1) == 1) res *= x;
            x *= x;
            b >>= 1;
        }
        return res;
    }
}
