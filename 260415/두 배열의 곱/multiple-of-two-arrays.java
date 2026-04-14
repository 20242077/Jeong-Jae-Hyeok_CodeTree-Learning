import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int rows = 3, cols = 3;
    int [][] arr_1 = new int[rows][cols], arr_2 = new int[rows][cols];

    for(int n = 0; n < 2; n++){
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if(n == 0){
                    arr_1[i][j] = sc.nextInt();
                }else{
                    arr_2[i][j] = sc.nextInt();
                }
            }
        }
    }
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            System.out.print(arr_1[i][j]*arr_2[i][j]+" ");
        }
        System.out.println();
    }
    }
}