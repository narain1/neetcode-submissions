class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> output;
        for (auto s: strs) {
            vector<int> count(26, 0);
            for (const auto &c: s) 
                count[c - 'a'] += 1;
            
            string key;
            for (auto o: count) {
                key += std::to_string(o);
                key += ",";
            }
            output[key].push_back(s);
        }
        vector<vector<string>> out;
        for (const auto& [k, v]: output) {
            out.push_back(v);
        }
        return out;
    }
};
