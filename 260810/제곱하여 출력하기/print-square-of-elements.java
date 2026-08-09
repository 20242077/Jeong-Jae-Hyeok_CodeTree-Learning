import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int[] arr = new int[num];
        for(int i=0;i<num;i++){
            int input = sc.nextInt();
            arr[i] = input*input;
        }
        for(int i=0;i<num;i++){
            System.out.print(arr[i]+" ");
        }
    }
}