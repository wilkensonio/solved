package icpcbook.noduplicate;

import java.util.HashMap;
import java.util.Map;

/**
 * https://open.kattis.com/problems/nodup?editresubmit=12369980
 */
import java.util.HashSet;
import java.util.Scanner;

class NoDuplicate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] words = sc.nextLine().split(" ");
        System.out.println(noDuplicate2(words));
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

    static String noDuplicate2(String[] words) {
        Map<String, Integer> seen = new HashMap<>();
        for (String word : words) {
            seen.putIfAbsent(word, 0);
            seen.put(word, seen.get(word) + 1);
        }

        for (Map.Entry<String, Integer> entry : seen.entrySet()) {
            System.out.println(entry.getKey());
            if (entry.getValue() > 1)
                return "yes";
        }
        return "no";
    }

}
