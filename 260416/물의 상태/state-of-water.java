import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력이 있을 때만 실행하도록 합니다.
        if (sc.hasNextInt()) {
            int n = sc.nextInt();

            // 1. 0도 미만인 경우
            if (n < 0) {
                System.out.println("ice");
            } 
            // 2. 100도 이상인 경우 (새로 추가된 조건)
            else if (n >= 100) {
                System.out.println("vapor");
            } 
            // 3. 그 외의 경우 (0도 이상 100도 미만)
            else {
                System.out.println("water");
            }
        }
        
        sc.close();
    }
}