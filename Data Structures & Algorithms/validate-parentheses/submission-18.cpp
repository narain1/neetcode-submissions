class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        unordered_map<char, char> d = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };
        for (const auto c: s) {
            if (d.count(c)) {
                stack.push_back(c);
            } else {
                if (stack.empty() || d[stack.back()] != c) {
                    return false;
                }
                stack.pop_back();
            }
        }
        return stack.empty();
    }
};
