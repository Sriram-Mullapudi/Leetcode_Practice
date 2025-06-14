class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        
        # Compute maximum
        max_val = num
        for d in '0123456789':
            replaced = num_str.replace(d, '9')
            max_val = max(max_val, int(replaced))
        
        # Compute minimum
        min_val = num
        for d in '0123456789':
            replaced = num_str.replace(d, '0')
            min_val = min(min_val, int(replaced))
        
        return max_val - min_val
