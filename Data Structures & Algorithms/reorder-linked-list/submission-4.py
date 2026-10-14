# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def printList(self, head):
        curr = head

        while curr: 
            print(curr.val)
            curr = curr.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not (head and head.next): return

        prev = None
        l1 = head
        l2 = head

        # Find the half of the list
        while l2 and l2.next: 
            prev = l1
            l1 = l1.next             
            l2 = l2.next.next
        prev.next = None

        # Reverse the second part of the list
        prev = None
        curr = l1

        while curr: 
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        h_1 = head
        h_2 = prev

        self.printList(h_1)
        self.printList(h_2)

        # Merge the two lists
        curr_1 = h_1
        curr_2 = h_2

        while curr_1:
            c2_next = curr_2.next
            curr_2.next = curr_1.next
            curr_1.next = curr_2

            curr_1 = curr_1.next.next
            if not curr_1:
                curr_2.next = c2_next
            else:
                curr_2 = c2_next

                





