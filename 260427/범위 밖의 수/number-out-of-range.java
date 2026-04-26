import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    System.out.print((a<10)||(a>20)?"yes":"no");
    sc.close();
    }
}