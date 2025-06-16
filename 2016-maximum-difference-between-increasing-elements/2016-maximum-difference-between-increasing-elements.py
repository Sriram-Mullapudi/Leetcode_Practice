def maximumDifference(nums):
    min_value = nums[0]
    max_diff = -1
    
    for num in nums[1:]:
        if num > min_value:
            max_diff = max(max_diff, num - min_value)
        else:
            min_value = num
            
    return max_diff
