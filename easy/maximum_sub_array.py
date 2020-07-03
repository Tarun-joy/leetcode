class Solution(object):
    def maxSubArray(self, nums):
        maxsum = totalsum = nums[0]
        for i in nums[1:]:
            totalsum = max(i,totalsum+i)
            maxsum = max(maxsum,totalsum)
        return maxsum
if __name__ == "__main__":
    a = Solution()
    x = a.maxSubArray([4,-1,2,1])
    print(x)
    pass


