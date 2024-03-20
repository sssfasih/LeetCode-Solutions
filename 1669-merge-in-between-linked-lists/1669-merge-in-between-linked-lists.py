class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        head = list1
        while head.next:
            if count == a-1:
                temp = head.next
                head.next = list2
            head = head.next
            if count<= a:
                count+=1
        while a <= b:
            temp = temp.next
            a +=1
        head.next = temp
        return list1
            
            
            
            
        