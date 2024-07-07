func missingNumber(nums []int) int {
    number:=map[int]bool{}
    for _,num:=range nums{
        number[num]=true
    }
    for i:=0;i<=len(nums);i++{
        if !number[i]{
            return i
        }
    }
    
    return -1
}