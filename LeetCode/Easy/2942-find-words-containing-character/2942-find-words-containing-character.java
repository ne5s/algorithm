import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> answerList = new ArrayList<>();

        for (int i = 0; i < words.length; i++) {
            if (words[i].contains(Character.toString(x))) {
                answerList.add(i);
            }
        }

        return answerList;
    }
}