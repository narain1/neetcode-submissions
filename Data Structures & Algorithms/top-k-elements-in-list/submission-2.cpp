class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> d;
        for (const auto n: nums) {
            d[n]++;
        }

        vector<pair<int, int>> count_pairs;
        for (const auto &pair: d) {
            count_pairs.push_back({pair.second, pair.first});
        }

        sort(count_pairs.rbegin(), count_pairs.rend());

        vector<int> arr;
        for (int i=0; i<k; i++) {
            arr.push_back(count_pairs[i].second);
        }
        return arr;
    }
};
