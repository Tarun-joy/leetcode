class Solution(object):
    def strStr(self, haystack, needle):
        a = haystack
        b = needle
        if len(b)==0:
            return 0  
        if b in a:
            for i in range(len(a)):
                if a[i:i+len(b)]==b:
                    return i 
        else:
           return -1
                
if __name__ == "__main__":
    a = Solution()
    x = a.strStr("hello","ll")
    print(x)
    pass

        
