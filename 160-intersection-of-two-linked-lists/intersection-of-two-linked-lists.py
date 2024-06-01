# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        hashset=set()
        while headA:
            hashset.add(headA)
            headA=headA.next
        while headB:
            if headB in hashset:
                return headB
            headB=headB.next
        return None        