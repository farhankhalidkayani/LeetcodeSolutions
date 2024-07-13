func maxFrequencyElements(nums []int) int {
    hashtable:=map[int]int{}
    for _,num:=range nums{
        hashtable[num]++
    }
    res:=0
    max:=0
    for _,num:=range nums{
        max=int(math.Max(float64(max),float64(hashtable[num])))
    }
    hashset:=map[int]bool{}
    for _,num:=range nums{
        if hashtable[num]==max && hashset[num]==false{
            res+=max
            hashset[num]=true
        }
    }
    return res
}