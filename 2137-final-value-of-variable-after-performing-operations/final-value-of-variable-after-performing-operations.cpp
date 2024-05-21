class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
       int answer=0;
       vector<string>::iterator itr;
        for(itr=operations.begin();itr!=operations.end();itr++){
if(*itr=="--X"){
    --answer;
}if(*itr=="++X"){
    ++answer;
}if(*itr=="X--"){
    answer--;
}if(*itr=="X++"){
    answer++;
}
        }
        return answer;
    }
};