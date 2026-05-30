# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive linked list solution

        # remember that for recursive problems, always think of it as breaking 
        # down the problem into sub problems until you cant anymore
        
        # base case is empty list
        if head is None:
            return None
        
        newHead = head
        if head.next is not None:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead