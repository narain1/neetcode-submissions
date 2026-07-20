class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int offset = 0;
        for (int i=0; i<nums.size(); i++) {
            if (nums[i] == val) {
                offset++;
            }
            else if (offset) {
                nums[i - offset] = nums[i];
            }
        }
        return nums.size() - offset;
    }
};