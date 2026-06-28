class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int ptr = 0;
        for (const auto n: nums) {
            if (n != val) {
                nums[ptr++] = n;
            }
        }
        return ptr;
    }
};