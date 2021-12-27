import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        // In case there is no solution, we'll just return null
        return null;
    }
}
// class Solution {
//     public int[] twoSum(int[] nums, int target) {
//         List<Integer> boxedNumsList = IntStream.of(nums).boxed().collect(Collectors.toList());
//         Map<Integer, Integer>indices = new HashMap<>();
//         List<Integer>remainders = new ArrayList<>();
//         for(Integer num : boxedNumsList){
//             remainders.add(target - num);
//         }
//         AtomicInteger index= new AtomicInteger(0);
//         int remainder = 0;
//         for(Integer num : boxedNumsList){
//             remainder = target - num;
//             indices.put(index.getAndIncrement(), (remainder * 2 != target) ? remainder : (Collections.frequency(remainders,remainder) > 1 ) ? remainder : Integer.MIN_VALUE);
//         }
//         List<Integer>res = indices.entrySet()
//             .stream()
//             .filter(entry -> boxedNumsList.contains(entry.getValue()))
//             .map(Map.Entry::getKey)
//             .collect(Collectors.toList());
//         return res.stream()
//             .mapToInt(Integer::intValue)
//             .toArray();

//     }
// }