```java
class Solution {
    public int solution(int[] numbers, int n) {
        int answer = 0;
        for (int num : numbers) {
            if (answer > n)
                return answer;
            answer += num;
        }
        return answer;
    }
}

```
