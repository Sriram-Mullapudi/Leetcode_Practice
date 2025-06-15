class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        for d in num_str:
            if d != '9':
                max_num = int(num_str.replace(d, '9'))
                break
        else:
            max_num = num  # already all 9's
        
        # For minimum value
        if num_str[0] != '1':
            min_num = int(num_str.replace(num_str[0], '1'))
        else:
            for d in num_str[1:]:
                if d != '0' and d != '1':
                    min_num = int(num_str.replace(d, '0'))
                    break
            else:
                min_num = num  # already minimal
        return max_num - min_num
