import java.util.Scanner;    
// 00
// 10 11
// 20 21 22
// 30 31 32 33
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int[][] arr = new int[4][4];
    int total = 0;

    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            arr[i][j] = sc.nextInt();
            if(j <= i){
                total += arr[i][j];
            }
        }
    }
    System.out.print(total);
    }
}