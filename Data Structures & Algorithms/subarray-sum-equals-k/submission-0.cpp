class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefix_sum;
        prefix_sum[0] = 1;
        int s = 0, result = 0;
        for (const auto n: nums) {
            s += n;
            if (prefix_sum.count(s - k)) {
                result += prefix_sum[s - k];
            }
            prefix_sum[s]++;
        }
        return result;
    }
};