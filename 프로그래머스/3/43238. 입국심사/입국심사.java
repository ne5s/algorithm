import java.util.Arrays;

class Solution {
    public long solution(int n, int[] times) {

        long left = 1; // 최소 시간
        long right = (long) n * getMax(times); // 최대 시간
        long answer = right;

        while (left <= right) {
            long mid = (left + right) / 2;
            if (canFinish(n, times, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return answer;
    }

    // 주어진 시간 내에 모든 사람을 심사할 수 있는지 판단하는 함수
    private boolean canFinish(int n, int[] times, long mid) {
        long total = 0;
        for (int time : times) {
            total += mid / time;
        }
        return total >= n;
    }

    // 심사 시간 배열에서 가장 큰 값을 반환하는 함수
    private long getMax(int[] times) {
        long max = times[0];
        for (int time : times) {
            if (time > max) {
                max = time;
            }
        }
        return max;
    }
}