import java.util.Scanner;

class CodeTree {
    String sCode;
    char mPoint;
    int time;
    public CodeTree(String sCode, char mPoint, int time){
        this.sCode = sCode;
        this.mPoint = mPoint;
        this.time = time;
    }

}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String sCode = sc.next();
        char mPoint = sc.next().charAt(0);
        int time = sc.nextInt();
        // Please write your code here.
        CodeTree codeTree = new CodeTree(sCode,mPoint,time);
        System.out.printf("secret code : %s\n",codeTree.sCode);
        System.out.printf("meeting point : %s\n",codeTree.mPoint);
        System.out.printf("time : %d\n",codeTree.time);
    }
}