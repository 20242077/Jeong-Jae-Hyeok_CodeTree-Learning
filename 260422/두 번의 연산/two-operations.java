import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    if(num % 2 == 1){
        num += 3;
        if(num % 3 == 0){
            num /= 3;
        }
    }else{
        if(num % 3 == 0){
            num /= 3;
        }
    }
    System.out.print(num);
    sc.close();
    }
}