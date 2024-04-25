# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        
        p1,p2 = head,head
        
        while p1.next:
            counter +=1
            
            if counter > n:
                p2=p2.next
                
            p1= p1.next
            
        if counter < n:
            return head.next
        
        else:
            p2.next = p2.next.next
            return head
        
        
        