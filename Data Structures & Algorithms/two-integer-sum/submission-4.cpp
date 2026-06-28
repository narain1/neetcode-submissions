class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        int diff;
        for (int i=0; i < nums.size(); i++) {
            diff = target - nums[i];
            if (map.count(diff)) {
                return {map[diff], i};
            }
            map.insert({nums[i], i});
        }
        return {};
    }
};
