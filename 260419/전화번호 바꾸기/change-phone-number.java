import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    String phoneNum = sc.next();
    String[] arr = phoneNum.split("-");
    System.out.printf("%s-%s-%s",arr[0],arr[2],arr[1]);
    sc.close();
    }
}