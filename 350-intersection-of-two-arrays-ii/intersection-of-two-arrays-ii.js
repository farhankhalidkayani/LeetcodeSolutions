/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    let hashtable2=new Map();
    
    for(let c of nums2){
        if(hashtable2.has(c)){
            hashtable2.set(c,hashtable2.get(c)+1);
        }
        else{
            hashtable2.set(c,1);
        }
    }
    let res=[];
    for(let c of nums1){
        if(hashtable2.has(c) && hashtable2.get(c)>0){
            res.push(c);
            hashtable2.set(c,hashtable2.get(c)-1);
        }
    }
    
    return res;
};