class Solution {
public:
    std::unordered_map<int, int> compliments;
    vector<int> twoSum(vector<int>& nums, int target) {
        auto idx = 0;
        for (const auto& num : nums) {
            auto compliment = target - num;
            if (compliments.contains(compliment)) {
                auto& compliments_idx = compliments[compliment];
                return {idx, compliments_idx};
            }
            compliments.insert(std::make_pair(num, idx));
            idx++;
        }
        return {};
    }
};