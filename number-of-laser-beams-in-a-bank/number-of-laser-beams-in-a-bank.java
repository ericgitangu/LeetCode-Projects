import java.util.*;
class Solution {
    public int numberOfBeams(String[] bank) {
        AtomicInteger a = new AtomicInteger(0);
        Map<Integer, Long> map = new HashMap<>();

        for(String row : bank) {
            Long val = row.chars().filter(ch -> ch == '1').count();
            if(!val.equals(0l))
                map.put(a.getAndIncrement(), val);
        }
        int res = 0;
        System.out.print(map);
        for(int x = 0; x < map.size() - 1; x++){
            res += map.get(x) * map.get(x+1);
        }
        return res;
    }
}