class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hash;
        for (auto i: nums) {
            // cout << hash.count(i);
            if (hash.count(i) == 1) return true;
            hash.insert(i);
        }
        return false;
    }
};