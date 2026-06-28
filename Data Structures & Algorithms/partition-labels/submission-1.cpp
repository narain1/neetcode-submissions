class Solution {
public:
    vector<int> partitionLabels(string s) {
        map<char, int> d;
        for (int i=0; i<s.size(); i++) {
            d[s[i]] = i;
        }

        int size = 0, end = 0;
        vector<int> res;

        for (int i=0; i<s.size(); i++) {
            size += 1;
            end = std::max(end, d[s[i]]);

            if (end == i) {
                res.push_back(size);
                size = 0;
            }
        }
       return res; 
    }
};
