import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] arr = new String[n];
        int sum = 0;
        int num = 0;
        for(int i=0;i<n;i++){
            arr[i] = sc.next();
            sum += arr[i].length();
            if(arr[i].charAt(0)=='a'){
                num+=1;
            }
        }
        System.out.printf("%d %d",sum,num);
    }
}