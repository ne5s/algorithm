import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public String solution(String p) {
        int left = 0;
        int right = 0;
        int splitI = 0;

        // 탈출 조건
        if (p.length() == 0) {
            return p;
        }


       // 균형적인 문자열 u 찾기
       for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left > 0 && left == right) {
                splitI = i;
                break;
            }
        }

        String u = p.substring(0, splitI + 1);
        String v = p.substring(splitI + 1);

        // u가 올바른 문자열이면, v를 재귀 호출한다
        if (isCollect(u)) {
            return u + solution(v);
        } else { // u가 올바른 문자열이 아니면, 주어진 조건대로 동작한다.
            StringBuilder sb = new StringBuilder();
            sb.append("(");
            sb.append(solution(v));
            sb.append(")");

            for (int i = 1; i < u.length() - 1; i++) {
                if (u.charAt(i) == '(') {
                    sb.append(')');
                } else {
                    sb.append('(');
                }
            }
            return sb.toString();
        }
    }

    // 스택을 이용해서 올바른 문자열인지 확인
    static boolean isCollect(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        if (!stack.isEmpty()) {
            return false;
        }
        return true;
    }
}