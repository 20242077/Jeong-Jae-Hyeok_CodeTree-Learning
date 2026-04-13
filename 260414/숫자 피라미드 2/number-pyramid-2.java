import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    int cnt = 0;
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= i; j++){
            System.out.print(j+cnt +" ");
        }
        cnt += i; // 첫줄 +0 둘째줄 0+1 셋째줄 0+1+2 넷째줄 0+1+2+3
        System.out.println();
    }
    }
}