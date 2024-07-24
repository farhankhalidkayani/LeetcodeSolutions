# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newHead=head.next
        prev=ListNode(0,head)
        while head and head.next:
            first=head
            second=head.next
            first.next=second.next
            second.next=first
            head=first.next
            prev.next=second
            prev=first
        return newHead

        