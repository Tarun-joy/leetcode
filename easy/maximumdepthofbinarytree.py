from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorder_traversal_iterative(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        print(root.right)
        stack, output = [root, ], []
        
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return output
if __name__=="__main__":
    # q = TreeNode()
    a = Solution()
    x = a.preorder_traversal_iterative([1,None,2,3])
    print(x)