class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        vector<int> a(26);
        for (int i=0; i<s.size(); i++) {
            a[s[i] - 'a']++;
            a[t[i] - 'a']--;
        }

        int sum = 0;
        for (int i=0; i < 26; i++) {
            sum += abs(a[i]);
        }

        return sum == 0;
    }
};
