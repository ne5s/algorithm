import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int maxPriority = Arrays.stream(priorities).max().getAsInt();
        int findNum = priorities[location];
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 0; i < priorities.length; i++) {
            deque.add(priorities[i]);
        }

        for (int i = 0; i < priorities.length; i++) {
            if (deque.getFirst() == maxPriority) {
                answer++;
                if (maxPriority == deque.pollFirst() && location == 0) return answer;
                maxPriority = deque.stream().max(Integer::compareTo).orElseThrow();
                location = location - 1 < 0 ? deque.size() - 1 : location - 1;
            } else {
                if (!deque.isEmpty()) {
                    deque.add(deque.poll());
                    location = location - 1 < 0 ? deque.size() - 1 : location - 1;
                }
            }
            i = -1;
        }
        return answer;
    }
}


