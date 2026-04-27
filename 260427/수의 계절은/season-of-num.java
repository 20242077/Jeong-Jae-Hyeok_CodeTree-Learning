import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int m = sc.nextInt();
    String s = "";
    if((m>=3)&&(m<=5)){
        s = "Spring";
    }else if((m>=6)&&(m<=8)){
        s = "Summer";
    }else if((m>=9)&&(m<=11)){
        s = "Fall";
    }else{
        s = "Winter";
    }
    System.out.print(s);
    sc.close;
    }
}