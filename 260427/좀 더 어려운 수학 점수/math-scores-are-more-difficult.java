import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int scMath1 = sc.nextInt(), scEng1 = sc.nextInt();
    int scMath2 = sc.nextInt(), scEng2 = sc.nextInt();
    if(scMath1==scMath2){
        System.out.print(scEng1>scEng2?"A":"B");
    }else{
        System.out.print(scMath1>scMath2?"A":"B");
    }
    sc.close();
    }
}
