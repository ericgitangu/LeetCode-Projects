#include <algorithm>
#include <utility>
#include <iostream>

class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        auto counter = 0;
        for(auto it = nums.begin(); it != nums.end(); it++ ){
            auto x = std::find(nums.begin(), nums.end(), *it + diff);
            if(x != nums.end()) {
                if(std::find(x, nums.end(), *x + diff) != nums.end()) {
                    counter++;
                }       
            } 
        }
        return counter;
    }
};