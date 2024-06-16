/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    let res1=[];
    let res2=[];
    let hashset1=new Set(nums1);
    let hashset2=new Set(nums2);
    for(c of hashset1){
        if(!hashset2.has(c)){
            res1.push(c);
        }
        
    }
    for(c of hashset2){
        if(!hashset1.has(c)){
            res2.push(c);
        }
        
    }
    return [res1,res2];
    
};