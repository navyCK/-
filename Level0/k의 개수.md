```java
class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String stringK = String.valueOf(k);
        for (int index = i; index <= j; index++) {
          if (String.valueOf(index).contains(stringK))
              answer+=countChar(String.valueOf(index), stringK.charAt(0));
      }
        return answer;
    }
    
    public static int countChar(String str, char ch) {
        return str.length() - str.replace(String.valueOf(ch), "").length();
    }
}

```
