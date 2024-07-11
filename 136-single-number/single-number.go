func singleNumber(nums []int) int {
   Counter:=map[int]int{}
   for _,num:=range nums{
        if _,ok:=Counter[num];ok{
            Counter[num]++
        }else{
            Counter[num]=1
        }}
        
    for _,num:=range nums{
        if Counter[num]==1{
            return num
        }
    }
    return 0
   }
   
