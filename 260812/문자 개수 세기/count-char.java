import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        char alp = sc.next().charAt(0);
        int n = 0;
        for(int i=0; i<str.length();i++){
            char alph = str.charAt(i);
            if(alph == alp){
                n++;
            }
        }
        System.out.print(n);
    }
}