import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int num = 8;
        double sum = 0.0;
        double avg = 0.0;
        double[] arr = new double[num];
        for(int i = 0; i<num; i++){
            arr[i] = sc.nextDouble();
            sum += arr[i];
        }
        avg = sum / num;
        System.out.printf("%.1f",avg);
    }
}