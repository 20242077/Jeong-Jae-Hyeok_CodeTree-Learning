import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[100];
        int cnt = 0;
        while(true){
            arr[cnt] = sc.nextInt();
            if(arr[cnt]==0){
                break;
            }
            cnt ++;
        }
        for(int i=0; i<cnt; i++){
            if(arr[i]%2==0){
                arr[i] /= 2;
            }else{
                arr[i]+=3;
            }
            System.out.print(arr[i]+" ");
        }
    }
}