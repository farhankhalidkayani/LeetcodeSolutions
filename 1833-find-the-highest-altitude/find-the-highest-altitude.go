func largestAltitude(gain []int) int {
    var res int
    if 0>gain[0]{
        res=0
    }else{
        res=gain[0]
    }
    for i:=1;i<len(gain);i++{
        gain[i]+=gain[i-1]
        if res<gain[i]{
            res=gain[i]
        }
    }
    return res
    
}