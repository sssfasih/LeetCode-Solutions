class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        copy = head
        while head:
            if head.val == val:
                head = head.next
                copy = head
            elif head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
            
        return copy