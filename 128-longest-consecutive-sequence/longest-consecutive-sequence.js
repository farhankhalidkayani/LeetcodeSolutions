/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let hashset=new Set([...nums]);
    let sequence=0;
    
    for(let num of nums){
        if(!hashset.has(num-1)){
            count=1;
            while(hashset.has(num+1)){
                num++;
                count++;
            }
            sequence=Math.max(count,sequence);
        }
    }

    return sequence;
};