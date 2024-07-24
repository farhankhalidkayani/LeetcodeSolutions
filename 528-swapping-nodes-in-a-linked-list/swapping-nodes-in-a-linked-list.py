# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first=head
        last=head
        fast=head
        for _ in range(k):
            fast=fast.next
        for _ in range(k-1):
            first=first.next
        while fast :
            fast=fast.next
            last=last.next
        first.val,last.val=last.val,first.val
        return head
        