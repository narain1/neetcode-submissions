class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs[0].length() == 1) {
            return strs[0];
        }

        sort(strs.begin(), strs.end());
        for (int i=0; i < min(strs[0].length(), strs.back().length()); i++) {
            if (strs[0][i] != strs.back()[i]) {
                return strs[0].substr(0, i);
            }
        }
        return strs[0];
    }
};