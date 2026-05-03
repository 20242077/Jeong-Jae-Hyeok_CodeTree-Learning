import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    while(a<=b){
        System.out.print(a+" ");
        if(a%2==0){
            a += 3;
        }else{
            a *= 2;
        }
    }
    sc.close();
    }
}