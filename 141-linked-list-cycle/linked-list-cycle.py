# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        hashset=set()
        while(head!=None):
            if head.next in hashset:
                return True
            hashset.add(head)
            head=head.next
        return False
        