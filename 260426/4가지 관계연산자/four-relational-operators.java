import java.util.Scanner;

class CodeTree{
    int a,b;
    CodeTree(int a,int b){
        this.a = a;
        this.b = b;
    }
        
    int show_1(){
        return a >= b ? 1:0;
    }
    int show_2(){
        return a > b ? 1:0;
    }
    int show_3(){
        return a <= b ? 1:0;
    }
    int show_4(){
        return a < b ? 1:0;
    }
}


public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt();
        CodeTree ct = new CodeTree(a,b);
        System.out.println(ct.show_1());
        System.out.println(ct.show_2());
        System.out.println(ct.show_3());
        System.out.println(ct.show_4());
        sc.close();
    }
}