# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next

        currsum=0
        Sum=0
        while stack:
            currsum=stack.pop(0)+stack.pop()
            if currsum>Sum:
                Sum=currsum
            
        return Sum

        