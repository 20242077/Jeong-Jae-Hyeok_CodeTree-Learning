import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), m = sc.nextInt();
    for(int i = n; i<=m; i+=2){
        System.out.print(i+" ");
    }
    sc.close();
    }
}