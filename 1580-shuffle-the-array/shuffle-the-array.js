/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let l=0;
    let r=n;
    let res=[];
    while(l<n && r<nums.length){
        res.push(nums[l]);
        res.push(nums[r]);
        l++;
        r++;
    }
    return res;
    
};