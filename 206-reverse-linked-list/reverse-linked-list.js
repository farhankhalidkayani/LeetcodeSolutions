/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let left=null;
    let right=head;
    while(right!=null){
        let temp=right.next;
        right.next=left;
        left=right;
        right=temp;
    }
    return left;
    
};