/**
 * @param {number} n
 * @return {number}
 */
 var answers=new Map()
var climbStairs = function(n) {
    if (n === 1) return 1;
    if (n === 2) return 2;
    if(answers.has(n)){
        return answers.get(n)
    }
     answers.set(n,climbStairs(n-1)+climbStairs(n-2))
     return answers.get(n)
};