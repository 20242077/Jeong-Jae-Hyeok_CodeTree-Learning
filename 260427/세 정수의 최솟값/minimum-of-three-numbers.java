import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt(); //3정수 입력받음
    int min = 0; //최솟값 변수 선언
    if(a<=b){
        if(a<=c){
            min = a;
        }else if(a>c){
            min = c;
        }
    }else if(a>=b){
        if(c>=b){
            min = b;
        }else if(c<b){
            min = c;
        }
    }
    System.out.print(min);
    sc.close();
    }
}