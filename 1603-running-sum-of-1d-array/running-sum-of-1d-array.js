/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let sum=[];
    let total=0
    for(let i=0;i<nums.length;i++){
        total+=nums[i];
        sum.push(total);
    }
    return sum;
};