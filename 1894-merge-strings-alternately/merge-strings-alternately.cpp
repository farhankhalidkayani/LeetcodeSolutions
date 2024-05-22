class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        int n=max(word1.size(),word2.size());
       
       
        for(int j=0;j<n;j++){
            if(j<word1.size()){
            result.push_back(word1[j]);}
            
             
            if(j<word2.size()){
            result.push_back(word2[j]);}
           
            
           
        }
        return result;
    }
};