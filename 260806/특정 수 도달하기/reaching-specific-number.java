import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int sum = 0;
        int count = 0;
        float avg = 0;
        for(int i = 0; i<10; i++){
            arr[i] = sc.nextInt();
            if(arr[i] >= 250){
                break;
            }
            sum += arr[i];
            count ++;
        }
        avg = (float) sum / count ;
        System.out.printf("%d %.1f",sum,avg);
    }
}