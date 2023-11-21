package icpcbook.BigInteger;

/**
 * https://open.kattis.com/problems/simpleaddition
 * 
 */

import java.math.BigInteger;
import java.util.Scanner;

class SimpleAdditon {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger a = new BigInteger(sc.next());
        BigInteger b = new BigInteger(sc.next());
        System.out.println(a.add(b));

        sc.close();
    }
}