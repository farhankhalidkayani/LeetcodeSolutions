func numJewelsInStones(jewels string, stones string) int {
    var m =map[rune]bool{}
    count:=0
    for _,jewel:=range jewels{
        m[jewel]=true
    }
    for _,stone:=range stones{
        if m[stone]{
            count++
        }
    }
    return count
}