class Solution {
public:
    int largestAltitude(vector<int>& gain) {
         vector<int> result(1,0);
        int ans=0;
        for(int i=0;i<gain.size();i++){
            
            ans=ans+gain.at(i);
            result.push_back(ans);

        }
        ans=0;
        for(int i=0;i<result.size();i++){
            
            if(ans<result.at(i)){
                ans=result.at(i);
            }

        }

        return ans;
    }
    
};