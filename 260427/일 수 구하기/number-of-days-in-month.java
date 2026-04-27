import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), result = 0;
    if(n==2){
        result = 28;
    }else if(((n<=7)&&(n%2==1))||(n>=8)&&(n%2==0)){
        result = 31;
    }else{
        result = 30;
    }
    System.out.print(result);
    sc.close();
    }
}