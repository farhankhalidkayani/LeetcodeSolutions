func minOperations(logs []string) int {
    res:=[]int{}
    for i,log:=range logs{
        if log=="../"{
            if len(res)!=0{
            res=res[:len(res)-1]
}        }else if log=="./"{
            continue
}else{
            res=append(res,i)
        }
    }
    return len(res)
}