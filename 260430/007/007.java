import java.util.Scanner;

class CodeTree {
    String sCode;
    String mPoint;
    int time;

    public CodeTree(String sCode, String mPoint, int time){
        this.sCode = sCode;
        this.mPoint = mPoint;
        this.time = time;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String sCode = sc.next();
        String mPoint = sc.next();
        int time = sc.nextInt();

        CodeTree ct = new CodeTree(sCode, mPoint, time);

        // 출력 형식 수정
        System.out.printf("secret code : %s\n", ct.sCode);
        System.out.printf("meeting point : %s\n", ct.mPoint); // %\ns -> %s\n 로 수정
        System.out.printf("time : %d\n", ct.time); // 마지막에도 줄바꿈(\n)을 넣어주는 것이 좋습니다.

        sc.close();
    }
}