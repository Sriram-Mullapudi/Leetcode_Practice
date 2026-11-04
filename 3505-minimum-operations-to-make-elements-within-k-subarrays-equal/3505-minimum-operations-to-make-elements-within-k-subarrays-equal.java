import java.util.*;
class Solution {
    public long minOperations(int[] nums, int x, int k) {
        int n = nums.length;

        //coordinate compression
        int[] sorted = nums.clone();
        Arrays.sort(sorted);

        int[] unique = new int[n];
        int m = 0;

        for (int v: sorted){
            if(m==0 || unique[m-1]!= v){
                unique[m++] = v;

            }
        }
        Fenwick count = new Fenwick(m);
        Fenwick sum = new Fenwick(m);

        long[] cost = new long[n-x+1];
        long windowSum = 0;

        //calculate cost for every window of size x

        for (int i = 0; i<n; i++){
            int idx = Arrays.binarySearch(
                unique, 0, m, nums[i]

            ) +1;
            count.add(idx, 1);
            sum.add(idx, nums[i]);
            windowSum += nums[i];

            if (i>= x){
                int oldIdx = Arrays.binarySearch(
                    unique, 0, m, nums[i-x]
                ) +1;

                count.add(oldIdx, -1);
                sum.add(oldIdx, -nums[i-x]);
                windowSum -= nums[i-x];
            }
            if(i>=x-1){
                int medianIdx = count.kth((x+1)/2);
                long median = unique[medianIdx - 1];

                long leftCount = count.query(medianIdx);
                long leftSum = sum.query(medianIdx);

                long rightCount = x - leftCount;
                long rightSum = windowSum - leftSum;

                cost[i-x+1] = median * leftCount - leftSum + rightSum - median * rightCount;
            }
        }

        //DP: Choose k non-overlappng windows
        long INF = Long.MAX_VALUE / 4;
        long[] prev = new long[n+1];

        for(int j = 1; j<=k; j++){
            long[] curr = new long[n+1];
            Arrays.fill(curr, INF);

            for (int i = j*x; i<=n; i++){
                //skip current position
                curr[i] = curr[i-1];

                //take window enfing at i-1
                curr[i] = Math.min(
                    curr[i],
                    prev[i-x] + cost[i-x]
                );
                }
                prev= curr;
            }
            return prev[n];
        }
        static class Fenwick {
            long[] tree;
            int n;

            Fenwick(int n){
                this.n=n;
                tree = new long[n+1];
            }
            void add(int i, long delta){
                while (i <= n) {
                    tree[i] += delta;
                    i+= i & -i;
                }
            }
            long query(int i){
                long result = 0;

                while(i>0){
                    result += tree[i];
                    i -= i& -i;
                }
                return result;
            }
            int kth(long k){
                int idx = 0;
                int bit = Integer.highestOneBit(n);

                while (bit >0){
                    int next = idx + bit;

                    if(next <= n && tree[next] < k){
                        idx = next;
                        k -= tree[next];
                    }
                    bit >>= 1;
                }
                return idx + 1;
            }
        }
        
    }
