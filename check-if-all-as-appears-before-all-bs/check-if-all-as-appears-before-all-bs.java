import java.util.*;
class Solution {
    public boolean checkString(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        String sorted = new String(chars);
        return new String(sorted).equals(s);
        
    }
}