class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, curr_xor):
            if i == len(nums):
                return curr_xor
            # Include or exclude nums[i]
            return dfs(i + 1, curr_xor ^ nums[i]) + dfs(i + 1, curr_xor)
        
        return dfs(0, 0)
