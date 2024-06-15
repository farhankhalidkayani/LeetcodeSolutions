/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let l=0;
    let r=0;
    
    while(r<t.length){
        if(s[l]==t[r]){
            l++;
            r++;
        }
        else{
            r++;
        }
    }
    if(l==s.length){
        return true;
    }
    else{
        return false;
    }
    
};