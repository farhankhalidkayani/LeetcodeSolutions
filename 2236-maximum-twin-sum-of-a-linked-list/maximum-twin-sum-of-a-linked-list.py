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

        left=0
        right=len(stack)-1
        Sum=0
        while left<right:
            if stack[left]+stack[right]>Sum:
                Sum=stack[left]+stack[right]
            left+=1
            right-=1
        return Sum

        