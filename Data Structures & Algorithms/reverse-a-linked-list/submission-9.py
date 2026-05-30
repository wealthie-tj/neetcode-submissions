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

        # assume we are working with [0, 1, 2, 3] for this explanation

        # the key to this problem is, focus when the subproblem is reversing a linked list
        # of [2, 3] and when reversing a linked list of [3].

        # reversing a linked list means there will always be a newHead -- the end of the list.
        # this is the value that should be returned by the reverseList function -> the new head
        # aka the end of the list. 

        # when linked list = [3], it will skip the if block and head.next = None which is 
        # valid when reversing a linkedlist of 1. that 1 entry will always have a next that 
        # points to None. furthermore, since this is the end of the list, it will be the 
        # new head. we need to store this value into a newHead variable and then return it.
        
        # when considering [2, 3], we want to execute code that a size 1 linked list should
        # not execute -- the if head.next block.
        # again, since we want newHead to have the value of the end of the list, we need to
        # set the variable both outside AND within the if block. 
        # this is where the newHead = self.reverseList(head.next) comes into play.
        # remember that reverseList should return the NEW HEAD OF THE REVERSED LINKED LIST.
        # ^^ which is fixed in every scenario. how do we know that newHead is fixed? well,
        # because we're not manipulating it. we're only setting it and then returning.

        # what we are actually manipulating are the pointers. in the case of [2, 3],
        # the head = 2. naturally, we will have access to 3 because 2.next = 3. 
        # in order to reverse this list, 3 (head.next) needs to have its next pointer 
        # point to 2 (head). this is where the 'head.next.next = head' comes from.
        # what happens afterwards is a step that needs to occur regardless of whether 
        # the head is of a size 2 linked list, or a size 1. (hence why it is outside if-block)
        # head (in this example it is 2) should point to None. 'head.next = None'
        # we again return the new head of this list, which is, unchangedly, 3.  

        # this will recursively happen and that's all we need to do. if we back a prev step,
        # we would need to reverse a linked list of [1, 2, 3].
        # head = 1, since head.next, we go into the if-block and newHead is set to 3.
        # head.next in this case is 2. 2's next pointer will be set to head, which is 1.
        # head.next will point to None. newHead is returned (still 3). and the cycle goes on.

        
        # base case is empty list
        if head is None:
            return None
        
        newHead = head
        if head.next is not None:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead