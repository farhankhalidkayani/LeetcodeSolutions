import "math"

func maximumWealth(accounts [][]int) int {
    res:=0
    for i:=0;i<len(accounts);i++{
        sum:=sum(accounts[i]...)
        res=int(math.Max(float64(res),float64(sum)))
    }
    return res
}
func sum(arr ...int) int{
    sum:=0
    for _,num:=range arr{
        sum+=num
    }
    return sum
}