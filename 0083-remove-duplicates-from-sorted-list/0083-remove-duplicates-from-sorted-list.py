# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:return None
        copy = head
        while head.next:
            if head.next.val== head.val:
                head.next = head.next.next
            else:
                head=head.next
        return copy
        