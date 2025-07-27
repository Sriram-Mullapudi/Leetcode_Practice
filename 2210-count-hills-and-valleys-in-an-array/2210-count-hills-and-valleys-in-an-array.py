class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        # Remove consecutive duplicates to simplify comparisons
        clean_nums = [nums[0]]
        for num in nums[1:]:
            if num != clean_nums[-1]:
                clean_nums.append(num)

        # Now go through the cleaned list and check each element (except first and last)
        for i in range(1, len(clean_nums) - 1):
            prev = clean_nums[i - 1]
            curr = clean_nums[i]
            next = clean_nums[i + 1]

            if curr > prev and curr > next:
                # It's a hill
                count += 1
            elif curr < prev and curr < next:
                # It's a valley
                count += 1

        return count
