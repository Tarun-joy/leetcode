class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif x< mid*mid:
                high = mid
            else:
                low = mid        
if __name__ == "__main__":
    a = Solution()
    x = a.mySqrt(4)
    print(x)
    pass