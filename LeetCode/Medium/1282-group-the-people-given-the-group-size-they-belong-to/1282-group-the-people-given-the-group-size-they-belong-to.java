import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        List<List<Integer>> answer = new ArrayList();
        List<Integer> midA = new ArrayList<>();
        List<Integer> visited = new ArrayList<>();
        int len = groupSizes.length;

        for (int i = 0; i < len; i++) {
            if (visited.indexOf(i) != -1) {
                continue;
            }
            if (groupSizes[i] == 1) {
                midA = new ArrayList<>();
                midA.add(i);
                visited.add(i);
                answer.add(midA);
                continue;
            }
            int count = groupSizes[i];
            int fixedCount = groupSizes[i];
            midA = new ArrayList<>();
            midA.add(i);
            visited.add(i);
            for (int j = i + 1; j < len; j++) {
                if (count == 1) {
                    break;
                }
                if (groupSizes[j] == groupSizes[i]) {
                    midA.add(j);
                    visited.add(j);
                    count--;
                }
            }
            answer.add(midA);
        }
        return answer;
    }
}