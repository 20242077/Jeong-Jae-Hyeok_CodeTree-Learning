import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    while(true){
        int n = sc.nextInt();
        if(n > 200 || n < -200){
            System.out.println("input -200 <= n <= 200");
        }else if(n < 0){
            System.out.println("ice");
            break;
        }else{
            System.out.println("water");
            break;
        }
    }
}
}