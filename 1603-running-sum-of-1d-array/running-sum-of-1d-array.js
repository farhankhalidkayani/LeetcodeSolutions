/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let sum=nums;
    for(let i=1;i<nums.length;i++){
        sum[i]+=sum[i-1];
    }
    return sum;
};