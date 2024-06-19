import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> answerList = new ArrayList<>();

        Arrays.sort(arr);

        for (int a : arr) {
            if (a % divisor == 0) answerList.add(a);
        }

        if (answerList.size() == 0) answerList.add(-1);

        return answerList.stream().mapToInt(i->i).toArray();
    }
}