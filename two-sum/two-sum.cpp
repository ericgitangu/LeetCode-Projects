class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int>indices;
        std::set<int>set;
        int i(0);
        for(int i(0); i < nums.size(); i++){
            int compliment =  target - nums.at(i);
            auto nth = set.insert(std::move(nums.at(i)));
            if(!nth.second){
                auto indexPtr = std::find(nums.begin(), nums.begin()+i, compliment);
                int index = (int)std::distance(nums.begin(), indexPtr);
                if(nums[index]+nums[i]==target){
                    indices.push_back(index);
                    indices.push_back(i);
                    return indices;
                }
            }
            set.insert(std::move(compliment)); //store the compliment.
        }
        return indices;
    }
};