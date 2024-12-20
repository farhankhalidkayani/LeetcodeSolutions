/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    let res=[];
    for(oper of operations){
        if(oper==="D"){
            let newScore=res[res.length-1]*2;
            res.push(newScore);
        }
        else if(oper==="C"){
            res.pop();
        }
        else if(oper==="+"){
            let num1=res[res.length-1];
            let num2=res[res.length-2];
            res.push(num1+num2);
        }
        else{
            res.push(Number(oper));
        }
    }
    let answer=0;
    for(num of res){
        answer+=num;
    }
    return answer;
};