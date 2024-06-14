# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp!=None:
            temp=temp.next
            count+=1
        count-=n
        temp=head
        if count==0:
            return head.next
        for i in range(count-1):
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        return head
        