func runningSum(nums []int) []int {
    res:=[]int{}
    total:=0
    for i:=0;i<len(nums);i++{
        total+=nums[i]
        res=append(res,total)
    }
    return res
}