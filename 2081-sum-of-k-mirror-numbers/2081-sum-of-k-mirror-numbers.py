class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_k_palindrome(num, k):
            base_k = []
            while num > 0:
                base_k.append(num % k)
                num //= k
            return base_k == base_k[::-1]

        def generate_palindromes():
            # odd-length palindromes
            for length in range(1, 20):  # long enough for n <= 30
                half = 10 ** ((length - 1) // 2)
                for root in range(half, 10 * half):
                    s = str(root)
                    if length % 2 == 0:
                        yield int(s + s[::-1])
                    else:
                        yield int(s + s[-2::-1])

        res = 0
        count = 0
        for num in generate_palindromes():
            if is_k_palindrome(num, k):
                res += num
                count += 1
                if count == n:
                    break
        return res
