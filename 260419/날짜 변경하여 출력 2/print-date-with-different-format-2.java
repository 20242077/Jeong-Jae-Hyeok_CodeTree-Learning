import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    String input = sc.next();
    String[] dateArr = input.split("-");
    int year = Integer.parseInt(dateArr[2]);
    int month = Integer.parseInt(dateArr[0]);
    int date = Integer.parseInt(dateArr[1]);
    System.out.printf("%d.%d.%d",year,month,date);

    sc.close();
    }
}