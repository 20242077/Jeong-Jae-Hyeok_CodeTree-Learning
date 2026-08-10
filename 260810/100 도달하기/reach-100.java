import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[20];
        int cnt =2;
        arr[0] = 1;
        arr[1] = n;
        for(int i=2; i<20; i++){
            arr[i] = arr[i-2] + arr[i-1];
            cnt ++;
            if(arr[i]>100){
                break;
            }
        }
        for(int i=0; i<cnt; i++){
            System.out.print(arr[i]+" ");
        }
    }
}