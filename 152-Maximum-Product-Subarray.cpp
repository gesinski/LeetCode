class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int result = *max_element(nums.begin(), nums.end());
        int curMax = 1;
        int curMin = 1;

        for (const auto& num : nums) {
            if (num == 0) {
                curMax = 1;
                curMin = 1;
                continue;
            }
            int tmp = curMax;
            curMax = max(max(curMax * num, curMin * num), num);
            curMin = min(min(tmp * num, curMin * num), num);
            
            if (curMax > result)
                result = curMax;
        }
        return result;
    }
};