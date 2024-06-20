/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let l=head;
    let r=head;
    while(r!=null &&r.next!=null){
        
        l=l.next;
        r=r.next.next;
        if(l==r){return true;}
    }
    return false;
    
};