class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int, int> mp;
        mp[0] = 1;
        int s = 0, result = 0;
        for (auto i: nums) {
            s += i;
            if (mp.contains(s - k)) {
                result += mp[s - k];
            }
            mp[s]++;
        }
        return result;
    }
};