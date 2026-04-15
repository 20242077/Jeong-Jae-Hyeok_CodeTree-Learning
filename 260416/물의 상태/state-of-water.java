import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 안내 메시지나 무한 루프 없이 한 번만 입력받습니다.
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            
            // 문제에서 요구하는 출력값만 딱 출력합니다.
            if (n < 0) {
                System.out.println("ice");
            } else {
                System.out.println("water");
            }
        }
        
        sc.close();
    }
}