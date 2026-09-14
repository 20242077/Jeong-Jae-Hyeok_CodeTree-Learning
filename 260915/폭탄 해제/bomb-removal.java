import java.util.Scanner;

class BombDisposal {
    String code;
    char color;
    int second ;

    public BombDisposal(String code, char color, int second){
        this.code = code;
        this.color = color;
        this.second = second;
    }
    
    public void show(){
        System.out.printf("code : %s\n",this.code);
        System.out.printf("color : %s\n",this.color);
        System.out.printf("second : %d\n",this.second);
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String uCode = sc.next();
        char lColor = sc.next().charAt(0);
        int time = sc.nextInt();
        // Please write your code here.
        BombDisposal bombDis = new BombDisposal(uCode, lColor, time);
        bombDis.show();
    }
}