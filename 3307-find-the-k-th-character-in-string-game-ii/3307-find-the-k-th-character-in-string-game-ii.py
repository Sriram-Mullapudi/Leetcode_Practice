class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        lengths = [1]  # Start with "a"
        
        # Compute length of string after each operation (clamp to k to avoid overflow)
        for op in operations:
            lengths.append(min(lengths[-1] * 2, k))
        
        shift = 0  # Net shifts applied through operation 1
        for i in range(len(operations) - 1, -1, -1):
            op = operations[i]
            half_len = lengths[i]
            
            if op == 0:
                if k > half_len:
                    k -= half_len  # came from 2nd half
            else:
                if k > half_len:
                    k -= half_len  # came from shifted part
                    shift += 1     # reverse shift will be needed

        # Final character is 'a' after reverse-shifting `shift` times
        return chr((shift % 26) + ord('a'))
