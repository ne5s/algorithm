import java.util.Arrays;

class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        Arrays.sort(seats);
        Arrays.sort(students);
        int answer = 0;
        int n = students.length;

        for (int i = 0; i < n; i++) {
            answer += Math.abs(seats[i] - students[i]);
        }
        return answer;
    }
}