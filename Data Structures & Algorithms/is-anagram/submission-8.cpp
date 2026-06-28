class Solution {
public:
    bool isAnagram(string s, string t) {
        std::array<int, 26> arr = {};
        if (s.length() != t.length()) return false;
        for (int i=0; i < s.length(); i++) {
            arr[s[i] - 'a'] += 1;
            arr[t[i] - 'a'] -= 1;
        }
        // int sum = std::accumulate(arr.begin(), arr.end(), 0);
        // return sum == 0;
        for (int x : arr) if (x != 0) return false;
        return true;
    }
};
