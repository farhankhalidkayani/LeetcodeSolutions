/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    prev:=head
    current:=head
    hashset:=map[int]bool{}
    for current!=nil{
        if _,ok:=hashset[current.Val];ok{
            prev.Next=current.Next
        }else{
            hashset[current.Val]=true
            prev=current
        }
        current=current.Next
    }
    return head
}