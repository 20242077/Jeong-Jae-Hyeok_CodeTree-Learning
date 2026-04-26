import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int a=sc.nextInt(),b=sc.nextInt(),c=sc.nextInt();
    int min = 0;
    if((a<=b)&&(a<=c)){
        min=a;
    }else if((b<=a)&&(b<=c)){
        min=b;
    }else{
        min=c;
    }
    System.out.print(min);
    sc.close();
    }
}