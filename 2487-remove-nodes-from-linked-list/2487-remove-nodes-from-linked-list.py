class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recursive(root):
            if root.next:
                delete = recursive(root.next)                
                if delete:
                    root.next = root.next.next                
                if root.next.val > root.val:
                    return True
            return False
        if recursive(head):
            head = head.next
        return head