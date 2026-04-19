import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int bot = sc.nextInt(), h = sc.nextInt();
    bot += 8;
    h *= 3;
    System.out.printf("%d\n%d\n%d",bot,h,bot*h);
    }
}