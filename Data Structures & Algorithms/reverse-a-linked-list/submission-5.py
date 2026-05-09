# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        curr = head
        prev = None
        next = None

        while curr is not None:
            # store the next value in the list so that we dont lose track of it
            next = curr.next

            # the curr.next should be pointing to the previous item on the list
            # the first iteration we want the curr.next to be None since it was the first
            # in the list but now it should be at the end
            curr.next = prev

            # now all our work is done, we just need to prep for the next iteration
            # in the next iteration, the curr will be seen as the prev, and the curr.next 
            # will be seen as the curr
            prev = curr
            curr = next

        # at the end of the iteration, curr will be at the end of the list and that will be stored
        # in the prev pointer. that will be the new head
        head = prev

        return head  
