import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int cnt=0; // 5의 배수 카운팅
        int num = 1; // 입력받은 배열 갯수 카운팅
        int[] arr = new int[100];
        arr[0] = sc.nextInt();
        if(arr[0]%5==0){
            cnt=1;
        }
        for(int i=1;i<100;i++){
            arr[i] = arr[0]*(i+1);
            num ++;
            if(arr[i]%5==0){
                cnt++;
            }
            if(cnt>=2){
                break;
            }
        }
        for(int i=0;i<num;i++){
            System.out.print(arr[i]+" ");
        }
    }   
}