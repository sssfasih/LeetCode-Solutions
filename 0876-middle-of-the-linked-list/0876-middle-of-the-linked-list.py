# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        copy=head
        while head.next:
            head= head.next
            n+=1
        n //= 2
        while n:
            copy = copy.next
            n-=1
        return copy