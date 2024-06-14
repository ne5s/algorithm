import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] shuffle(int[] nums, int n) {
        List<Integer> newNumsList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            newNumsList.add(nums[i]);
            newNumsList.add(nums[i + n]);
        }
        return newNumsList.stream().mapToInt(i -> i).toArray();
    }
}