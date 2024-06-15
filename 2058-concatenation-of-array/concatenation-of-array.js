/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let n=nums.length;
    const res=[...nums];
    for(let i=0;i<n;i++){
        nums.push(res[i]);
    }
    return nums
};