class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Total sum from 1 to n
        total_sum = n * (n + 1) // 2
        
        # Count of numbers divisible by m in range [1, n]
        count = n // m
        
        # Sum of all numbers divisible by m using arithmetic progression formula
        divisible_sum = m * count * (count + 1) // 2
        
        # Non-divisible sum = total sum - divisible sum
        non_divisible_sum = total_sum - divisible_sum
        
        return non_divisible_sum - divisible_sum
   