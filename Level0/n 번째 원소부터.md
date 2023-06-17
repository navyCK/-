```java
class Solution {
    public int[] solution(int[] num_list, int n) {
        int size = num_list.length - n + 1;
        int index = 0;
        int[] answer = new int[size];
        for (int i=0; i<size; i++) {
            answer[index] = num_list[i+n-1];
            index++;
        }
            
        return answer;
    }
}
```
