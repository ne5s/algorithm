import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[][] jobs) {
        // 작업 시작 시간으로 정렬
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);

        int nowTime = 0; // 현재 시간
        int total = 0; // 총 작업 완료 시간 합
        int index = 0; // jobs 배열을 순회할 index
        int jobsNum = jobs.length;
        // 작업의 소요 시간으로 정렬하는 우선순위 큐
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);

        while (index < jobsNum || !pq.isEmpty()) {
            // 현재 시간 이내에 요청이 들어온 작업을 모두 우선순위 큐에 넣음
            while (index < jobsNum && jobs[index][0] <= nowTime) {
                pq.offer(jobs[index]);
                index++;
            }

            if (!pq.isEmpty()) {
                int[] job = pq.poll();
                nowTime += job[1];
                total += nowTime - job[0];
            } else {
                // 대기 중인 작업이 없으면 다음 작업 시작 시간으로 시간 업데이트
                nowTime = jobs[index][0];
            }
        }
        return total / jobsNum;
    }
}