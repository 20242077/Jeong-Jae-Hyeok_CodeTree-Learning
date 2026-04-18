import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    String t = sc.next();
    String[] strArr = t.split(":");
    int h = Integer.parseInt(strArr[0]), m = Integer.parseInt(strArr[1]);
    System.out.printf("%d:%d",h+1,m);
    }
}