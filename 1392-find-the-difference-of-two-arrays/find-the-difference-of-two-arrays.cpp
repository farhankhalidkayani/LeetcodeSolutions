class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
         vector<int> answer1;
    vector<int> answer2;
    bool flag;
    
    int n=nums1.size();
    int m=nums2.size();
        
        
       


    for(int i=0;i<n;i++){
        flag=0;
        for(int j=0;j<m;j++){
            
            if(nums1[i]==nums2[j]){
                flag=1;
                break;
            }
        }
        if(!flag){
            answer1.push_back(nums1[i]);
        }
    }

    
    for(int i=0;i<m;i++){
        flag=0;
        for(int j=0;j<n;j++){
            if(nums2[i]==nums1[j]){
                flag=1;
                break;
            }
        }
        if(!flag){
            answer2.push_back(nums2[i]);
        }

    }
             n=answer1.size();
             m=answer2.size();
               for(int i=0;i<n;i++){
        
        for(int j=i+1;j<n;j++){
            
            if(answer1[i]==answer1[j]){
                answer1.erase(answer1.begin()+j);
                n--;
                j--;
            }
        }
       
        }
               for(int i=0;i<m;i++){
        
        for(int j=i+1;j<m;j++){
            
            if(answer2[i]==answer2[j]){
                answer2.erase(answer2.begin()+j);
                m--;
                j--;
            }
        }
       
        }
    vector<vector<int>> answer={answer1,answer2};
    return answer;

        
    }
};