import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    String input = sc.next();
    String[] ymd = input.split("\\.");
    System.out.printf("%s-%s-%s",ymd[1],ymd[2],ymd[0]);

    sc.close();
    }
}