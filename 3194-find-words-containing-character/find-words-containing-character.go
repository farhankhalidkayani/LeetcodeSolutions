func findWordsContaining(words []string, x byte) []int {
    res:=[]int{}
    for i,word:=range words{
        if strings.Contains(word,string(x)){
            res=append(res,i)
        }
    }
    return res
}