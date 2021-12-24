class Solution {
private:
    int closest = 0;
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        std::sort(nums.begin(), nums.end());
        int min = std::numeric_limits<int>::max(), delta = std::numeric_limits<int>::max();
        for(int i = 0; i < nums.size(); i++){
            int start = i + 1;
            int stop = nums.size() - 1;
            
            while(start < stop){
                int sum = nums[i] + nums[start] + nums[stop];
                // cout<<nums[i]<<", "<<nums[start]<<", "<<nums[stop];
                delta = abs(target - sum);
                if(delta < min){
                    closest = sum;
                    min = delta;
                }
                if(sum <= target) {
                    start++;
                }
                if(sum >= target) {
                    stop--;
                }
            }
        }
        return closest;
    }
};