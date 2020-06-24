class Solution(object):
    def isPalindrome(self, x):
        if(x < 0 or (x % 10 == 0 and x == 0)) : return False
        reverted = 0
        while x>reverted:
            reverted = reverted* 10 + x%10
            x = x//10
            print(x,reverted,"$$$$$$$$$$$")
        print(x,reverted,"$$$$$$$$$$$")
        return x == reverted or x == reverted//10
if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome(1221))
    pass

        
