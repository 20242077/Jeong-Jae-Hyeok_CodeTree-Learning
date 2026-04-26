import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int a=sc.nextInt(),b=sc.nextInt(),c=sc.nextInt();
    int min = 0;
    if((a<=b)&&(a<=c)){
        min=a;
    }else if((a<=b)&&(a>=c)){
        min=c;
    }else if((a>=b)&&(b>=c)){
        min=c;
    }else if((a>=b)&&(b<=c)){
        min=b;
    }
    System.out.print(min);
    sc.close();
    }
}