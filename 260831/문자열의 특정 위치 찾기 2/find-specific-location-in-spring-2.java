import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    String[] arr = new String[] {"apple","banana","grape","blueberry","orange"};
    char word = sc.next().charAt(0);
    int num = arr.length;
    int n = 0;
    for(int i = 0; i<num; i++){
        if(word == arr[i].charAt(2) || word == arr[i].charAt(3)){
            n++;
            System.out.println(arr[i]);
            }
        }
        System.out.print(n);
    }
}