import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    String word = sc.next();
    String ans;
    if(word.equals("S")){
        ans = "Superior";
    }else if(word.equals("A")){
        ans = "Excellent";
    }else if(word.equals("B")){
        ans = "Good";
    }else if(word.equals("C")){
        ans = "Usually";
    }else if(word.equals("D")){
        ans = "Effort";
    }else{
        ans = "Failure";
    }

    System.out.print(ans);
    }
}