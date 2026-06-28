class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> d;
        for (int i=0; i<nums.size(); i++) {
            int n = nums[i];
            if (d.count(n) && abs(d[n] - i) <= k) {
                return true;
            }
            d[n] = i;
        }
        return false;
        
    }
};