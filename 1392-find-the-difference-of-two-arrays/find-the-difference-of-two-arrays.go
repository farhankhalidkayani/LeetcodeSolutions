func findDifference(nums1 []int, nums2 []int) [][]int {
    hashtable1 := map[int]bool{}
    hashtable2 := map[int]bool{}
    done1:=map[int]bool{}
    done2:=map[int]bool{}
    res := [][]int{}

    // Fill hashtable1 with elements from nums1
    for _, num := range nums1 {
        hashtable1[num] = true
    }

    // Fill hashtable2 with elements from nums2
    for _, num := range nums2 {
        hashtable2[num] = true
    }

    // Find elements in nums1 that are not in nums2
    var res1 []int
    for _, num := range nums1 {
        if !hashtable2[num] && !done2[num]{
            res1 = append(res1, num)
            done2[num]=true
        }
    }

    // Append the result to res
    res = append(res, res1)

    // Find elements in nums2 that are not in nums1
    var res2 []int
    for _, num := range nums2 {
        if !hashtable1[num] && !done1[num] {
            res2 = append(res2, num)
            done1[num]=true
        }
    }

    // Append the result to res
    res = append(res, res2)

    return res
}