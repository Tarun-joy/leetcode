class Solution(object):
    def isValid(self, strs):
        
        stack = []
        mapping = {"}":"{",")":"(","]":"["}

        for char in strs:
            if char in mapping:
                topelement = stack.pop() if stack else "#"

                if mapping[char] != topelement:
                    return False
            else:
                stack.append(char)
        return not stack

if __name__ == "__main__":
    a = Solution()
    x = a.isValid("{{{{}}}}")
    print(x)
    pass

        
