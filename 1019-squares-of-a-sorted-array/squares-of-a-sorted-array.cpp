class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n=nums.size();
        for(int i=0;i<n;i++){
            nums[i]=nums[i]*nums[i];
        }
        for(int k=1;k<n;k++){
            bool flag=0;
            for(int i=0;i<n-k;i++){
                if(nums[i]>nums[i+1]){
                 int temp=nums[i];
                 nums[i]=nums[i+1];
                 nums[i+1]=temp;
                 flag=1;
                }
            }
            if(flag==0){
                break;
            }
        }
   return nums; }
};