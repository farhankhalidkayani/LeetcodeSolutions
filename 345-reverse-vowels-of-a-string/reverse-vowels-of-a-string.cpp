class Solution {
public:
    string reverseVowels(string s) {
        int left = 0;
        int right = s.size() - 1;
        string vowels = "aeiouAEIOU";

        while (left < right) {
            // Move left pointer until we find a vowel
            while (left < right && vowels.find(s[left]) == string::npos) {
                left++;
            }
            // Move right pointer until we find a vowel
            while (left < right && vowels.find(s[right]) == string::npos) {
                right--;
            }
            // Swap the vowels
            if (left < right) {
                swap(s[left], s[right]);
                left++;
                right--;
            }
        }
        return s;
    }
};
