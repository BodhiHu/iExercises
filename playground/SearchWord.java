import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import java.util.regex.Pattern;
import java.lang.Character;

// HJ27 查找兄弟单词
// input: 3 abc bca cab abc 1
public class SearchWord {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        while (in.hasNextInt()) { // 注意 while 处理多个 case
            int count = in.nextInt();
            List<String> words = new ArrayList<>();
            for (int i = 0; i < count; i++) {
                words.add(in.next());
            }
            String search = in.next();
            int k = in.nextInt();

            // System.out.println(count + ", " + words + ", " + search + ", " + k);

            Set<String> searchSet = new HashSet<>(Arrays.asList(search.split("")));

            List<String> matchedWords = new ArrayList<>();
            for (int i = 0; i < count; i++) {
              String w = words.get(i);
              if (search.equals(w)) {
                continue;
              }

              if (searchSet.equals(new HashSet<String>(Arrays.asList(w.split(""))))) {
                matchedWords.add(w);
              }
            }

            // System.out.println(matchedWords);

            matchedWords.sort(null);

            if (matchedWords.size() > k) {
              System.out.println(matchedWords.get(k));
            } else {
              System.out.println("-null");
            }

            break;
        }
    }
}
