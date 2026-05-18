use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();
        for(idx, &num) in nums.iter().enumerate() {
            let compliment = target - num;
            if let Some(&comp_idx) = map.get(&compliment) {
                return vec![comp_idx, idx as i32];
            }
            map.insert(num, idx as i32);
        }
        return vec![]
    }
}