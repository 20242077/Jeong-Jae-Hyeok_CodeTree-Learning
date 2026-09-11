import java.util.Scanner;
public class Main {
    public static boolean hasDiv3(int n){
        if(n%3==0){
            return true;
        }
        else{
            return false;
        }
    }

    public static boolean getFunc(int n){
        int temp = n;
        while(temp>0){
            if((temp%10==3)||(temp%10==6)||(temp%10==9)){
                return true;
            }
            temp = temp/10;
        }
        return false;        
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        // Please write your code here.
        int cnt = 0;
        for(int i=A; i<=B; i++){
            if(hasDiv3(i)||getFunc(i)){
                cnt ++;
            }
        }
        System.out.print(cnt);
    }
}