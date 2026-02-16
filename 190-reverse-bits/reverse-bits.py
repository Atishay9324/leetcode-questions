class Solution:
    def reverseBits(self, n: int) -> int:
        b = ''
        for i in range(32):
            b  = b + str(n%2)
            n = n//2
        result = int(b,2)
        return result
        