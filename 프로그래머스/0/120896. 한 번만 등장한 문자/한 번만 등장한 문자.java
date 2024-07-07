import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuffer sb = new StringBuffer();
        Map<String, Integer> map = new HashMap<>();
        List<String> list = new ArrayList<>();

        for (String h : s.split("")) {
            map.put(h, map.getOrDefault(h, 0) + 1);
        }
        if (!map.isEmpty()) {
            for (Map.Entry<String, Integer> entry : map.entrySet()) {
                if (entry.getValue() == 1) {
                    list.add(entry.getKey());
                }
            }
        }
        Collections.sort(list);

        for (int i = 0; i < list.size(); i++) {
            sb.append(list.get(i));
        }
        return sb.toString();
    }
}