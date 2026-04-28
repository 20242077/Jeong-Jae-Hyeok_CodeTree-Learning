import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt(), b = sc.nextInt();
    for(int i = a; i>=b; i--){
        System.out.print((i%2==0)?i+" ":"");
    }
    sc.close();
    }
}