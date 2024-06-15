/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s=s.toLowerCase().replace(/[^a-z0-9]/gi,'');
    let res=s.split('').reverse().join('');
    return s==res;
};