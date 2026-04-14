import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int rows = sc.nextInt(); // 행의 개수 입력받기
    int cols = sc.nextInt(); // 열의 개수 입력받기
    int [][] arr_1 = new int[rows][cols], arr_2 = new int[rows][cols];

    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            arr_1[i][j] = sc.nextInt();
        }
    }
    
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            arr_2[i][j] = sc.nextInt();
        }
    }

    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            if(arr_1[i][j] == arr_2[i][j]){
                System.out.print(0+" ");
            }else{
                System.out.print(1+" ");
            }
        }
        System.out.println();
    }
    sc.close();
    }
}