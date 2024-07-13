func numberOfEmployeesWhoMetTarget(hours []int, target int) int {
    res:=0
    for _,num:=range hours{
        if num>=target{
            res++
        }
    }
    return res
}