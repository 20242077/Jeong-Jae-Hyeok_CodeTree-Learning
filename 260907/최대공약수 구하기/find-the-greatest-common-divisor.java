import java.util.Scanner;

public class Main {
    public static void printMaxMin(int n, int m){
        int max = 0, lcm = 0;
        if(n>=m){
            max = n;
        }else{
            max = m;
        }
        for(int i=1; i<=max; i++){
            if((m % i == 0)&&(n % i == 0)){
                lcm = i;
            }
        }
        System.out.print(lcm);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        // Please write your code here.
        printMaxMin(n,m);    
    }
}