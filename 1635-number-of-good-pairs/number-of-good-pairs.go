func numIdenticalPairs(nums []int) int {
    count:=0
    for index1,num1:=range nums{
        for index2,num2:=range nums{
            if num1==num2 && index1<index2{
                count++
            }
        }
    }
    return count
}