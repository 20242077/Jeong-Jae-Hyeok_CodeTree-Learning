import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int age1 = sc.nextInt();
    String gen1 = sc.next();

    int age2 = sc.nextInt();
    String gen2 = sc.next();

    if((age1>=19)&&(gen1.equals("M"))||(age2>=19)&&(gen2.equals("M"))){
        System.out.print(1);
    }else{
        System.out.print(0);
    }
    sc.close();
    }
}