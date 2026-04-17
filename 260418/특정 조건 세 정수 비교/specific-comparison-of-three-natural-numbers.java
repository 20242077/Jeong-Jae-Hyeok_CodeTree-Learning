import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        // 1. 첫 번째 조건: a가 최솟값인가?
        if (a <= b && a <= c) {
            System.out.print(1 + " ");
        } else {
            System.out.print(0 + " ");
        }

        // 2. 두 번째 조건: 세 수가 모두 같은가?
        if (a == b && b == c) {
            System.out.print(1);
        } else {
            System.out.print(0);
        }
    }
}