import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    String num = sc.next();
    String[] numArr = num.split("-");
    
    int numFront = Integer.parseInt(numArr[0]);
    int numBack = Integer.parseInt(numArr[1]);
    System.out.printf("%d%d",numFront,numBack);

    sc.close();
    }
}