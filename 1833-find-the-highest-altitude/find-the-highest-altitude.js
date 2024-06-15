/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let total=0;
    let max=0;
    for(let i=0;i<gain.length;i++){
        total+=gain[i];
        max=Math.max(max,total);
    }
    return max;
    
};