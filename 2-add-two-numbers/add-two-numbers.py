# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1=0
        number2=0
        place=1
        place1=1
        while l1!=None:
            number1+=l1.val*place
            place*=10
            l1=l1.next
        while l2!=None:
            number2+=l2.val*place1
            place1*=10
            l2=l2.next
        result=number1+number2
        if result==0:
            return ListNode()
        dummy=ListNode()
        Head=dummy
        while result>0:
            rem=result%10
            result//=10
            Head.next=ListNode(rem)
            Head=Head.next
        return dummy.next

        