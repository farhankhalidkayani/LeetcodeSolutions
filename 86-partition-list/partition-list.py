# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1=ListNode(0)
        dummy2=ListNode(0)
        temp1=dummy1
        temp2=dummy2
        current=head
        while current:
            if current.val<x:
                temp1.next=current
                temp1=current
            else:
                temp2.next=current
                temp2=current
            current=current.next
        temp1.next=dummy2.next
        temp2.next=None
        return dummy1.next

        