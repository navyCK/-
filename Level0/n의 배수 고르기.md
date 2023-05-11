```java
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int n, int[] numlist) {
        int[] answer;
        ArrayList<Integer> list = new ArrayList<>();
        for (int num : numlist) {
            if (num % n == 0)
                list.add(num);
        }
        int size = list.size();
        answer = new int[size];
        for (int i=0; i<size; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}

```
