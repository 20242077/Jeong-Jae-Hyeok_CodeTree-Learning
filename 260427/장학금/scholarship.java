import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int mid = sc.nextInt(), fin = sc.nextInt();
    int money = 0;
    if(mid>=90){
        if(fin>=95){
            money = 100000;
        }else if(fin>=90){
            money = 50000;
        }
    }
    System.out.print(money);
    sc.close();
    }
}