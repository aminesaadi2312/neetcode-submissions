# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        while head : 
            heap.append(head.val)
            head = head.next
        if not heap :
            return None
            
        reverse = ListNode()
        res = reverse
        while heap : 
            reverse.val = heap.pop()
            if heap : 
                reverse.next = ListNode()
                reverse = reverse.next
        return res