class Solution {
    public int[] solution(int[] numbers, String direction) {
        switch (direction) {
            case "left":
                int temp = numbers[0];
                for (int i = 0; i < numbers.length - 1; i++) {
                    numbers[i] = numbers[i + 1];
                }
                numbers[numbers.length - 1] = temp;
                break;
            case "right":
                int tmp = numbers[numbers.length - 1];
                for (int i = numbers.length - 2; i >=0; i--) {
                    numbers[i + 1] = numbers[i];
                }
                numbers[0] = tmp;
                break;
        }
        return numbers;
    }
}