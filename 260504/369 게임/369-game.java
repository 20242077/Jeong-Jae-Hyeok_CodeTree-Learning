import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    for(int i = 1; i <= N; i++){
        int temp = i;
        boolean has369 = false;
        if(i % 3 == 0){
            has369 = true;
        }
        while(temp > 0){
            int digit = temp % 10;
            if((digit==3)||(digit==6)||(digit==9)){
                has369 = true;
                break;
            }
            temp /= 10;
        }
        System.out.print((has369)? 0:i);
        System.out.print(" ");
    }
    sc.close();
    }
}