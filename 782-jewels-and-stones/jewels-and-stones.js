/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    let j=new Set(jewels);
    let count=0;
    for(c of stones){
        if(j.has(c)==true){
            count++;
        }
    }
    return count;
};