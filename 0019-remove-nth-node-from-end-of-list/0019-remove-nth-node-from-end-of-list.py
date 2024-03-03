# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        p1,p2 = head,head
        
        while p1.next:
            p1= p1.next
            count +=1
            if count > n:
                p2=p2.next
            
        if count < n:
            return head.next
        else:
            p2.next = p2.next.next
            return head
        
        
        