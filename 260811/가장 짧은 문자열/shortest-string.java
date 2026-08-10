import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String str1 = sc.next();
        int len1 = str1.length();
        String str2 = sc.next();
        int len2 = str2.length();
        String str3 = sc.next();
        int len3 = str3.length();
        int max = len1;
        int min = len1;
        if(len2 > max) max = len2;
        if(len3 > max) max = len3;

        if(len2 < min) min = len2;
        if(len3 < min) min = len3;

        int result = max - min;
        System.out.print(result);

    }
}