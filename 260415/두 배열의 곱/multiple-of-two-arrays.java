import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rows = 3, cols = 3;
        int[][] arr_1 = new int[rows][cols];
        int[][] arr_2 = new int[rows][cols];

        // 첫 번째 행렬 입력
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                arr_1[i][j] = sc.nextInt();
            }
        }

        // 두 번째 행렬 입력
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                arr_2[i][j] = sc.nextInt();
            }
        }

        // 결과 출력 (곱셈과 출력을 동시에 수행)
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print((arr_1[i][j] * arr_2[i][j]) + " ");
            }
            System.out.println();
        }

        sc.close(); // 자원 해제
    }
}