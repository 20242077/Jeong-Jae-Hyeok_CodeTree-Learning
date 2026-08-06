import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int subject = sc.nextInt();
        double sum = 0.0;
        double avg = 0.0;
        double[] arr = new double[subject];
        
        for(int i=0; i<subject; i++){
            arr[i] = sc.nextDouble();
            sum += arr[i];
        }
        avg = sum / subject ;
        if(avg >= 4.0){
            System.out.printf("%.1f\nPerfect",avg);
        }else if(avg >= 3.0){
            System.out.printf("%.1f\nGood",avg);
        }else{
            System.out.printf("%.1f\nPoor",avg);
        }
    }
}