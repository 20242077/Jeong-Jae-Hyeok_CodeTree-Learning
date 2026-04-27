import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int y = sc.nextInt();
    boolean result = true;
    if(y%4==0){
        if((y%100==0)&&(y%400!=0)){
            result = false;
        }
    }else{
        result = false;
    }
    System.out.print(result);
    sc.close();
    }
}