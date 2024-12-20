/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let closing=new Map()
    closing.set("}","{")
    closing.set("]","[")
    closing.set(")","(")
    let res=[]
    for(bracket of s){
        if(closing.has(bracket)&&res[res.length-1]===closing.get(bracket)){
            res.pop();
        }else{
            res.push(bracket);
        }
    }
    console.log(res.length)
    return res.length===0;

};