class MyQueue{
    constructor(){
        this.stack=[];
    }
    push(value){
        this.stack.push(value);
    }
    pop(){
        return this.stack.shift();
    }
    peek(){
        return this.stack[0];
    }
    empty(){
        if(this.stack.length==0){
            return true;
        }
        else{
            return false;
        }
    }
}