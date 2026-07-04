class Solution {
public:
    bool checkValidString(string s) {
        int low = 0, high = 0;
        for (char a: s) {
            if (a == '(') {
                low++;
                high++;
            } else if (a == ')') {
                low--;
                high--;
            } else {
                low--;
                high++;
            }
            if (high < 0) { return false; }
            low = max(low, 0);
        }
        return low == 0;
    }
};
