func moveZeroes(nums []int)  {
    nonZero:=0
    for i:=0;i<len(nums);i++{
        if nums[i]!=0{
            nums[nonZero]=nums[i]
            nonZero++
        }
    }
    for nonZero<len(nums){
        nums[nonZero]=0
        nonZero++
    }
}