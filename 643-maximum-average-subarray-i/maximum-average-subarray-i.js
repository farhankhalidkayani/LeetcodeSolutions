/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let sum=0;
    let maxsum=-1*Number.MAX_VALUE;
    let hashset=new Set();
    let l=0;
    for(let r=0;r<nums.length;r++){
        if(r-l+1>k){
            sum-=nums[l];
            hashset.delete(nums[l]);
            l++;
        }
        hashset.add(nums[r]);
        sum+=nums[r];
        if(r-l+1===k){
            maxsum=Math.max(maxsum,sum/k);
        }
    }
    return maxsum;
};