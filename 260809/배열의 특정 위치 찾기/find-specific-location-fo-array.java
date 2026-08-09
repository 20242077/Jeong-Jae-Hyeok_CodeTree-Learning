import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int sumEven = 0;
        int sumOdd = 0;
        int numOdd = 0;
        for(int i=0; i<10; i++){
            arr[i] = sc.nextInt();
            if((i+1)%2==0){
                sumEven += arr[i];
            }
            if((i+1)%3==0){
                sumOdd += arr[i];
                numOdd += 1;
            }
        }
        double evgOdd = (double)sumOdd / numOdd;
        System.out.printf("%d %.1f",sumEven,evgOdd);
    }
}