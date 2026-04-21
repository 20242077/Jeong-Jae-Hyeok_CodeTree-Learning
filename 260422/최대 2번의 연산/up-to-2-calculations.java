import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    int result = 0;
    if(num % 2 == 0){
        result = num/2;
        if(result % 2 == 1){
            result = (result +1)/2;
        }
    }else{
        result = (num+1)/2;
    }
    System.out.print(result);
    sc.close();
    }
}