/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    if(s.length!=t.length){
        return false;
    }
    hashtables={};
    hashtablet={};
    
    for(let i=0;i<s.length;i++){
        if((s[i] in hashtables && hashtables[s[i]]!=t[i])||(t[i] in hashtablet && hashtablet[t[i]]!=s[i])){
            return false;
        }
        hashtables[s[i]]=t[i];
        hashtablet[t[i]]=s[i];
    }
    return true;

};