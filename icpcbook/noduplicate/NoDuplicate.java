package icpcbook.noduplicate;

/**
 * https://open.kattis.com/problems/nodup?editresubmit=12369980
 */
import java.util.HashSet;
import java.util.Scanner;

class NoDuplicate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] words = sc.nextLine().split("");
        System.out.println(noDuplicate(words));
        sc.close();

    }

    static String noDuplicate(String[] words) {
        HashSet<String> seen = new HashSet<>();

        for (String word : words) {
            if (seen.contains(word))
                return "no";
            seen.add(word);
        }
        return "yes";
    }
}
