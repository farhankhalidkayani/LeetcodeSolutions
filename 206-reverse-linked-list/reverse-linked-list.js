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
function revList(curr,prev){
    if(curr==null){
        return prev
    }
    let temp=curr.next
    curr.next=prev
    prev=curr
    curr=temp
    return revList(curr,prev)
}
var reverseList = function(head) {
    
    prev=null
    curr=head
    return revList(curr,prev)
};