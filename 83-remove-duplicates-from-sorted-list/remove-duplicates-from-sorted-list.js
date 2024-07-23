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
var deleteDuplicates = function(head) {
    let hashset=new Set();
    let prev=new ListNode(0);
    let current=head;
    while(current){
        if(hashset.has(current.val)){
            prev.next=current.next;
        }
        else{
            prev=current;
            hashset.add(current.val);
        }
        current=current.next
    }
    return head;
};