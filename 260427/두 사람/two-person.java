import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int age1 = sc.nextInt();
    String gen1 = sc.next();
    int age2 = sc.nextInt();
    String gen2 = sc.next();

    if((age1>=19)||(age2>=19)){
        if((gen1.equals("M"))||(gen2.equals("M"))){
            System.out.print(1);
        }else{
            System.out.print(0);
        }
    }else{
        System.out.print(0);
    }
    sc.close();
    }
}