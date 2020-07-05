class Solution:
    def merge(self, nums1: [int], m: int, nums2:[int], n: int) -> None:
        
        if n==0:
            return 
        nums1[-n:] = nums2
        nums1.sort()
        return nums1
if __name__ == "__main__":
    a = Solution()
    x = a.merge([1,2,3,0,0,0,0],4,[2,5,6,7],4)
    print(x)
    pass