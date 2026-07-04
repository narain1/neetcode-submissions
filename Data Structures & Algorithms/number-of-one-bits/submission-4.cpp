class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        for (int bit=31; bit>=0; bit--) {
            if ((n >> bit) & 1 ){
                count++;
            }
        }
        return count;

    }
};
