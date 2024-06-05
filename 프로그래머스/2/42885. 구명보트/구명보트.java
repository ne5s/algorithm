import java.util.Arrays;

class Solution {
    public static int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        int start = 0;

        for (int i = people.length - 1; i >= start; i--) {
            if (people[start] + people[i] <= limit) {
                start++;
                answer++;
            } else {
                answer++;
            }
        }
        return answer;
    }
}