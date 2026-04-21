import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int money = sc.nextInt();
    if(money >= 3000){
        System.out.print("book");
    }else if(money >= 1000){
        System.out.print("mask");
    }else if(money >= 500){
        System.out.print("pen");
    }else{
        System.out.print("no");
    }
    sc.close();
    }
}