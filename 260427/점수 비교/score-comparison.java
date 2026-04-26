import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int aMath = sc.nextInt(), aEng = sc.nextInt();
    int bMath = sc.nextInt(), bEng = sc.nextInt();
    System.out.print((aMath>bMath)&&(aEng>bEng)?1:0);
    sc.close();
    }
}