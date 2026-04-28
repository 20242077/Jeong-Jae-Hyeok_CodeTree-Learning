import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), i = 1;
    while(true){
        if(i>n){break;}
        System.out.print(i+" ");
        i += 1;
    }
    sc.close();
    }
}