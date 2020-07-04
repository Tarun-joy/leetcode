class Solution(object):
    def plusOne(self, digits):
        digits = list(map(str,digits))
        digits = "".join(digits)
        digits = str(int(digits)+1)
        lst = []
        for i in digits:
            lst.append(int(i))
        return lst
if __name__ == "__main__":
    a = Solution()
    x = a.plusOne([1,2,5])
    print(x)
    pass
