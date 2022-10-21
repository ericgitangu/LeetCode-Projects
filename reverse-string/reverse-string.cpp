class Solution {
public:
    void reverseString(vector<char>& s) {
        auto left = 0, right = int(s.size()) -1;
        while(left < right) {
            swap(s[left++],s[right--]);
        }
    }
};