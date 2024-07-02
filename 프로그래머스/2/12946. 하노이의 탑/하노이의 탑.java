import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] solution(int n) {
        List<int[]> answerList = new ArrayList<>();

        List<int[]> result = hanoi(n, 1, 3, 2);

        return result.stream().toArray(int[][]::new);
    }
    
    public List<int[]> hanoi(int n, int from, int to, int other) {
        if (n == 0) return null;
        if (n == 1) {
            List<int[]> result = new ArrayList<>();
            result.add(new int[]{from, to});
            return result;
        }

        List<int[]> result = hanoi(n - 1, from, other, to);
        result.add(new int[]{from, to});
        result.addAll(hanoi(n - 1, other, to, from));
        return result;
    }
}