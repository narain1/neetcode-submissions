class Solution {
public:
    void sortColors(vector<int>& nums) {
        int ptr1 = 0, ptr2 = nums.size() - 1;
        int ptr = 0;
        while (ptr <= ptr2) {
            if (nums[ptr] == 0) {
                swap(nums[ptr1], nums[ptr]);
                ptr1++;
            }
            else if (nums[ptr] == 2) {
                swap(nums[ptr2], nums[ptr]);
                ptr2--;
                ptr--;
            } 
            ptr++;
        }
    }
};