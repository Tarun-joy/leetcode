class Solution:
    def mySqrt(self, x: int) -> int:
        x = x^1/2
        return int(x)

if __name__ == "__main__":
a = Solution()
x = a.mySqrt(4)
print(x)
pass