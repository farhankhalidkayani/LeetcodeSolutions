/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let l=0;
    let r=0;
    while(r<chars.length){
        let count=0;
        let curr=chars[r];
        while(r<chars.length && curr==chars[r]){
            r++;
            count++;
        }
        chars[l++]=curr;
        if(count>1){
            for(let digit of count.toString()){
                chars[l++]=digit;
            }
        }
    }
    return l;
};