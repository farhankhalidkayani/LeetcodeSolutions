class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n= nums.size();
        int answer=0;
        sort(nums.begin(),nums.end());
        vector<int>::iterator itr;
       
for(int i=0;i<=n;i++){
    itr=find(nums.begin(),nums.end(),i);
    if(itr==nums.end()){
        answer=i;
    }
}
        
        return answer;
    }
};