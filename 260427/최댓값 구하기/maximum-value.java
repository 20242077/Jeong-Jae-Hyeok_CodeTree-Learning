import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int a=sc.nextInt(), b=sc.nextInt(), c=sc.nextInt();
    int max = a;

    if(max<=b){
        max = b;
        if(max<=c){
            max = c;
        }
    }else if(max<=c){
        max = c;
    }
    System.out.print(max);
    sc.close();
    }
}