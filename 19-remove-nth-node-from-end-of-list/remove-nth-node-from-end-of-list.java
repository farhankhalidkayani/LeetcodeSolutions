/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head.next==null){
            return null;
        }
        ListNode fast=head;
        ListNode slow=head;
        ListNode prev=head;
        for(int i=0;i<n;i++){
            
            fast=fast.next;
            if(fast==null){
                ListNode temp=head;
                head=head.next;
                temp.next=null;
                return head;
            }
        }
        while(fast!=null){
            prev=slow;
            fast=fast.next;
            slow=slow.next;
        }
        ListNode temp=prev.next!=null?prev.next:null;
        prev.next=prev.next!=null?prev.next.next:null;
        if(temp!=null){
            temp.next=null;
        }
        return head;

    }
}