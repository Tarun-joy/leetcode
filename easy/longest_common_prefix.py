class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return "" 
        
        minlen = len(strs[0])
        for i in range(len(strs)):
            minlen = min(len(strs[i]),minlen)  
        lcp = ""
        i = 0
        while i <minlen:
            char = strs[0][i]
            for j in range(1,len(strs)):
                if char != strs[j][i]:
                    return lcp
            lcp = lcp + char
            i = i+1
        return lcp


if __name__ == "__main__":
    a = Solution()
    x = a.longestCommonPrefix(["flower","flow","flight"])
    print(x)
    pass

        
