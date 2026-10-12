# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Return if head is None
        if not (head and head.next): return
        
        # Find the last one and the prev one
        curr = head
        prev = None
        while curr and curr.next:
            prev = curr 
            curr = curr.next
        
        if prev:
            prev.next = None
        curr.next = head.next
        head.next = curr

        self.reorderList(head.next.next)





        