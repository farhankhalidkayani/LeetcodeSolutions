/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let dummy= new ListNode(-1);
    let res=dummy;
    while(list1!==null && list2!==null){
        if(list1.val<list2.val){
            res.next=new ListNode(list1.val);
            list1=list1.next;
            res=res.next;
        }else{
            res.next=new ListNode(list2.val);
            list2=list2.next;
            res=res.next;
        }
    }
    if(list1!==null){
        res.next=list1;
    }
    if(list2!==null){
        res.next=list2;
    }
    return dummy.next;
};