class Solution {
public:
    // solution with hash map
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_pos;

        for (int pos2 = 0; pos2 < nums.size(); pos2++) {
            
            int diff = target - nums[pos2];
            
            if (num_pos.find(diff) != num_pos.end()) 
                return {num_pos[diff], pos2};

            num_pos[nums[pos2]] = pos2;
        }
        return {};
    }
};