class Solution(object):
    def removeDuplicates(self, nums):
        lennum = len(nums)
        if lennum == 0:
            return 0
        targetindex = 1
        og = nums[0]
        for i in range(1,lennum):
            if nums[i] != og:
                og = nums[i]
                print(og,"!!!!!!!!!")
                nums[targetindex] = nums[i]
                print(nums[targetindex],"$$$$$$$$$$$$$$$$")
                targetindex += 1
        
        return targetindex
        

if __name__ == "__main__":
    a = Solution()
    x = a.removeDuplicates([1,2,2,4,4,5,5])
    print(x)
    pass

        
