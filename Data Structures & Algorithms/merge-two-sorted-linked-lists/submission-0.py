# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = list1
        curr_2 = list2
        curr_3 = None
        
        if not (curr_1 and curr_2):
            if curr_1: return curr_1
            elif curr_2: return curr_2
            else: return None

        if curr_1.val < curr_2.val:
            curr_3 = curr_1
            curr_1 = curr_1.next
        else: 
            curr_3 = curr_2
            curr_2 = curr_2.next
        
        head = curr_3

        while curr_1 or curr_2:
            if curr_1 and curr_2:
                if curr_1.val < curr_2.val: 
                    curr_3.next = curr_1
                    curr_1 = curr_1.next
                else: 
                    curr_3.next = curr_2
                    curr_2 = curr_2.next
            else:
                if curr_1:
                    curr_3.next = curr_1
                    curr_1 = curr_1.next
                else: 
                    curr_3.next = curr_2
                    curr_2 = curr_2.next

            curr_3 = curr_3.next

        return head