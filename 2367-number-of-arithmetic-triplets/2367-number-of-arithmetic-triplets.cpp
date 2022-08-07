#include <algorithm>

class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        auto counter = 0;
        for(auto it = nums.begin(); it != nums.end(); it++ ){
            auto third = std::find(nums.begin(), nums.end(), *it + diff);
            if(third != nums.end()) {
                if(std::find(third, nums.end(), *third + diff) != nums.end()) {
                    counter++;
                }       
            } 
        }
        return counter;
    }
};