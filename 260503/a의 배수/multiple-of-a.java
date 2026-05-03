import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt(), a = sc.nextInt();
    int cnt = 1;
    while(cnt <= N){
        System.out.println((cnt % a == 0) ? 1 : 0);
        cnt += 1;
    }
    sc.close();
    }
}