import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int a=sc.nextInt(), b=sc.nextInt(), c=sc.nextInt();
    int mid = 0;
    if(a<=b){
        if(b<=c){
            mid = b;
        }else{
            if(a<=c){
                mid = c;
            }else{
                mid = a;
            }
        }
    }else{
        if(a<=c){
            mid = a;
        }else{
            if(b>=c){
                mid = b;
            }else{
                mid = c;
            }
        }
    }
    System.out.print(mid);
    sc.close();
    }
}