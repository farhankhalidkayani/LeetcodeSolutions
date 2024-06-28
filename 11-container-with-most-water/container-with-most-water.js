/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left=0;
    let right=height.length-1;
    let max=0;
    while(left<=right){
        let water=right-left;
        let cont=Math.min(height[left],height[right]);
        cont=water*cont;
        max=Math.max(cont,max);
        if(height[left]<height[right]){
            left++;
        }
        else{
            right--;
        }
    }
    return max;
};