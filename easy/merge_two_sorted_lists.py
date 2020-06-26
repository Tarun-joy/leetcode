class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        l1 = ListNode(l1)
        l2 = ListNode(l2)
        head = ListNode(0)
        ptr = head
        
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ptr.next = l2
                break
            elif l2 is None:
                ptr.next  = l1
                break
            else:
                smallervalue = 0
                if l1.val<l2.val:
                    smallervalue = l1.val
                    l1 = l1.next
                else:
                    smallervalue = l2.val
                    l2 = l2.next
            newnode = ListNode(smallervalue)
            ptr.next = newnode
            ptr = ptr.next
            print(head)
        return head.next

if __name__ == "__main__":
    a = Solution()
    x = a.mergeTwoLists([1,2,4],[1,3,4])
    print(x)
    pass

        
