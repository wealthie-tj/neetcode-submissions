# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        curr1 = list1
        curr2 = list2

        while curr1 and curr2 is not None:

            if curr1.val <= curr2.val:
                node.next = curr1
                curr1 = curr1.next
            else:
                node.next = curr2
                curr2 = curr2.next
            
            # move the node pointer for the dummy forward as well so no overrides happen
            node = node.next 

        if curr1 is None:
            node.next = curr2
        else:
            node.next = curr1
        
        return dummy.next