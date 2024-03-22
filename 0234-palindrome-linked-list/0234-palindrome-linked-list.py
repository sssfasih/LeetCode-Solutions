# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #tortoise and hare algorithm
        slow,fast =head,head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        
        #reverse Linked list
        prev = None
        while slow.next:
            temp= slow.next
            slow.next = prev
            prev=slow
            slow=temp
        slow.next = prev
        
        # Traverse two lists simultaneously
        while head and slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
        
        
            
        