import java.util.Scanner;

public class Main {
    public static int getGCD(int a,int b){
        while(b!=0){
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    public static void getLCD(int n,int m){
        int lcd = (n * m) / getGCD(n,m);
        System.out.print(lcd);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        // Please write your code here.
        getLCD(n,m);
    }
}