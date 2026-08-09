import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int sumOdd = 0, sumEven = 0;
        for(int i=0;i<10;i++){
            arr[i] = sc.nextInt();
            if((i+1)%2==0){
                sumEven+=arr[i];
            }else{
                sumOdd+=arr[i];
            }
        }
        int result = sumEven - sumOdd;
        if(result<0){
            result *= -1;
        }
        System.out.println(result);
    }
}