/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let NonZeroIndex=0;
    for(let i=0;i<nums.length;i++){
    if(nums[i]!=0){
        nums[NonZeroIndex]=nums[i];
        NonZeroIndex++;
    }
    }
    for(let i=NonZeroIndex;i<nums.length;i++){
    nums[i]=0;
    }
};