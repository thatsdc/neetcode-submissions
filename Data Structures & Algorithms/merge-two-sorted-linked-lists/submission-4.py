# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Manage when one of the lists is at the end (or also empty)
        if list1 is None: 
            return list2
        if list2 is None:
            return list1

        # Manage when both the lists have at least an element
        if list1.val <= list2.val:
            # Take list1 as smaller and recursively call the function skipping
            # the just set list1 element  
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2