class Solution {
    public int solution(String s) {
        String[] alpa = new String[]{"zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"};

        for (int i = 0; i < alpa.length; i++) {
            s = s.replace(alpa[i], String.valueOf(i));
        }

        return Integer.parseInt(s);
    }
}