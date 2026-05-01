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

    void show(){
        System.out.printf("secret code : %s\n",sCode);
        System.out.printf("meeting point : %s\n",mPoint);
        System.out.printf("time : %d",time);    
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String sCode;
        String mPoint;
        int time;
        // Please write your code here.
        sCode = sc.next();
        mPoint = sc.next();
        time = sc.nextInt();
        CodeTree ct = new CodeTree(sCode , mPoint , time);
        ct.show();
        sc.close();
    }
}