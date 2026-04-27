import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int scMath1 = sc.nextInt(), scEng1 = sc.nextInt();
    int scMath2 = sc.nextInt(), scEng2 = sc.nextInt();
    String name = "";
    if(scMath1 >= scMath2){
        if(scEng1>=scEng2){
            name = "A";
        }else{
            name = "B";
        }
    }else{
        name = "B";
    }
    System.out.print(name);
    sc.close();
    }
}
