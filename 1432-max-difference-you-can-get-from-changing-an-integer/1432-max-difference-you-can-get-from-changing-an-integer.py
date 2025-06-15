class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        
        # Max part
        for d in num_str:
            if d != '9':
                max_num = int(''.join(['9' if ch == d else ch for ch in num_str]))
                break
        else:
            max_num = num
        
        # Min part
        if num_str[0] != '1':
            d = num_str[0]
            min_num = int(''.join(['1' if ch == d else ch for ch in num_str]))
        else:
            for d in num_str[1:]:
                if d != '0' and d != '1':
                    min_num = int(''.join(['0' if ch == d else ch for ch in num_str]))
                    break
            else:
                min_num = num

        return max_num - min_num
