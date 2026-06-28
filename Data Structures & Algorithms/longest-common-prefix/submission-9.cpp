class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        for (int i=0; i<strs[0].length(); i++) { // characters over first string
            for (const string &s : strs) { // iterating over strings
                if (i == s.length() || strs[0][i] != s[i]) {
                    return s.substr(0, i);
                }
            }
        }
        return strs[0];
    }
};