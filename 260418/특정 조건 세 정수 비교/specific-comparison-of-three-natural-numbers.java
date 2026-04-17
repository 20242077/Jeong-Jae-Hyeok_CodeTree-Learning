import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if((a-b>0)||(a-c>0)){//이때 둘 중 하나라도 음수가 나오면 0출력 (a - b < 0) || (a - c < 0) 사용 --> 음수 판별 끝

            System.out.print(0+" ");
        }else if(((a-b==0)&&(a-c<0))||((a-c==0)&&(a-b0))){
            System.out.print(1+" ");
        }else if((a==b)&&(b==c)){
            System.out.print(0+" ");
        }

        if((a==b)&&(b==c)){
            System.out.print(1);
        }else{
            System.out.print(0);
        }
    }
}
