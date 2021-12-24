class Solution {
private:
    int vol{0};
public:
    int maxArea(vector<int>& height) {
        for(vector<int>::iterator left = height.begin(), right = height.end() - 1; left < right; ){
            int min = std::min(*left, *right), distance = std::distance(left, right), area = min * distance;
            vol = (area > vol) ? area : vol ;
            // cout<<vol<<", ";
            if(*left < *right){
                left++;
            } else {
                right--;
            }
        }
        return vol;
    }
};