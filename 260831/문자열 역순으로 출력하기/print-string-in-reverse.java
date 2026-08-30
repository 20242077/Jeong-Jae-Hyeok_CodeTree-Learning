import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    String[] arr = new String[4];
    int num = arr.length;
    for(int i=0; i<num; i++){
        String str = sc.next();
        arr[i] = str;
    }
    for(int i = num-1; i>=0; i--){
        System.out.println(arr[i]);
    }
    }
}