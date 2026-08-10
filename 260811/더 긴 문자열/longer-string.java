import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String str1 = sc.next();
        String str2 = sc.next();
        int len1 = str1.length();
        int len2 = str2.length();
        if(len1 > len2){
            System.out.printf("%s %d",str1,len1);
        }else if(len1==len2){
            System.out.print("same");
        }else{
            System.out.printf("%s %d",str2,len2);
        }
    }
}