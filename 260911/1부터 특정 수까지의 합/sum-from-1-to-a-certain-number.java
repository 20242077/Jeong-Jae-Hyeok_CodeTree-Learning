import java.util.Scanner;
public class Main {
    public static void printNum(int n){
        int num = 0;
        for(int i=1; i<=n; i++){
            num +=i;
        }
        System.out.print(num/10);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // Please write your code here.
        printNum(n);
    }
}