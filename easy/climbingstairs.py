class Solution:
    def climbStairs(self, n: int) -> int:
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # d ={1:1,2:2}
        # for i in range(3,n+1):
        #     val = d[i-1]+d[i-2]
        #     d[i] = val
        # return d[n]
        if n<=1:
            return 1
        first = 1
        second = 2
        for i in range(3,n+1):
            temp = first + second
            first = second
            second = temp
        return second
if __name__ == "__main__":
    a = Solution()
    x = a.climbStairs(5)
    print(x)
    pass