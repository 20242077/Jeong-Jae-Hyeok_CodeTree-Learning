import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String[] arr = new String[10];
        for(int i=0; i<10; i++){
            arr[i] = sc.next();
        }

        char alph = sc.next().charAt(0);
        int n = 0;
        for(int i=0;i<10;i++){
            int lastIndex = arr[i].length()-1;
            if(arr[i].charAt(lastIndex) == alph){
                System.out.println(arr[i]);
                n++;
            }
        }
        if(n==0){
            System.out.print("None");
        }
    }
}