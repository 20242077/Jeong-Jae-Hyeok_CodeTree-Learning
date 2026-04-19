import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int height = sc.nextInt();
    int weight = sc.nextInt();
    double bmi = (10000 * weight) / height * height;

    if((int)bmi >= 25){
        System.out.printf("%d\nObesity",(int)bmi);
    }else{
        System.out.printf("%d",(int)bmi);
    }
    sc.close();
    }
}
