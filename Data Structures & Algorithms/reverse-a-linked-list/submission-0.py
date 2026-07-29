# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head # 0

        while curr:
            temp = curr.next # 1
            curr.next = prev # 1 turns to None
            prev = curr # none turns to head 0, head.next is None
            curr = temp # 

        return prev
        