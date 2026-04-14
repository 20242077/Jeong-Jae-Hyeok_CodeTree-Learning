import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int rows = 3, cols = 3;
    int [][] arr = new int[rows][cols];

    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            arr[i][j] = sc.nextInt();
            System.out.print(arr[i][j]*3+" ");
        }
        System.out.println();
    }
    }
}