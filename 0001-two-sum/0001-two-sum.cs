public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int>map = new();
        int idx = 0;
        foreach (var num in nums){
            int compliment = target - num;
            if(map.TryGetValue(compliment, out int compIdx)){
                return new [] {idx, compIdx};
            }
            map.TryAdd(num, idx++);
        }
        return Array.Empty<int>();
    }
}