class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        n = head
        while n != None:
            v = 2*n.val
            if v > 9:
                if p == None:
                    p = ListNode(1)
                    head = p
                    p.next = n
                else:
                    p.val += 1
                n.val = v%10
            else:
                n.val = v
            p = n
            n = n.next

        return head 