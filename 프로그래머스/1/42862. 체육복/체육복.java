import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        List<Integer> nonLostReserve = new ArrayList<>();
        for (int a : reserve) {
            for (int b: lost) {
                if (a == b) {
                    nonLostReserve.add(a);
                }
            }
        }
        Arrays.sort(lost);
        Arrays.sort(reserve);

        for (int l : lost) {
            for (int r : reserve) {
                if (!nonLostReserve.contains(r) && !nonLostReserve.contains(l)) {
                    if ((l - 1) == r || (l + 1) == r) {
                        answer++;
                        nonLostReserve.add(r);
                        break;
                    }
                }
            }
        }
        return n - lost.length + nonLostReserve.size();
    }
}