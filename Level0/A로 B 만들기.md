```java
class Solution {
    public int solution(String before, String after) {
        int answer = 0;
        char[] charArrayBefore = before.toCharArray();
        
        for (char word : charArrayBefore) {
          if (after.contains(String.valueOf(word)))
              after = after.replaceFirst(String.valueOf(word), "");
        }
      
        if (after.equals(""))
            return 1;
        else
            return 0;
    }
}
```
