# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy=ListNode()
        tail=dummy
        while head:
            if head.next and (head.val==head.next.val):
                head.next=head.next.next
                continue
            tail.next=head
            head=head.next
            tail=tail.next
        return dummy.next
            
            
            
        