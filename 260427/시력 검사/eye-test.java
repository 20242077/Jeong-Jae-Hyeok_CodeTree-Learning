import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    double a = sc.nextDouble(), b = sc.nextDouble();
    String sight ;
    if((a>=1.0)&&(b>=1.0)){
        sight = "High";
    }else if((a>=0.5)&&(b>=0.5)){
        sight = "Middle";
    }else{
        sight = "Low";
    }
    System.out.print(sight);
    sc.close();
    }
    
}