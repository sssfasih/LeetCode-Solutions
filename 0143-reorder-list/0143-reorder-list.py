class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        while fast.next:
            fast = fast.next
            
        while head != fast:
            fast.next = head.next
            head.next = fast
            while fast.next != head.next:
                fast=fast.next
            head = head.next.next
        head.next = None
        
        