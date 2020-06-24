class Solution(object):
    def reverse(self,x):
        q = str(x)
        a = ""
        for i in q[::-1]:
            a = a + i   
        return(int(a))
if __name__ == "__main__":
    c= Solution()
    a = c.reverse(123456)
    print(a)
    pass

