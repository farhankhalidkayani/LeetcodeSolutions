func buildArray(nums []int) []int {
    res:=[]int{}
    for i:=0;i<len(nums);i++{
        res=append(res,nums[nums[i]])
    }
    return res

}