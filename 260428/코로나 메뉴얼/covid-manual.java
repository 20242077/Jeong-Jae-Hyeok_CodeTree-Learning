import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int a = 0, b = 0, c = 0, d = 0;

    for(int i = 0; i<3; i++){
        String sym = sc.next(), rst = "";
        int temp = sc.nextInt();

        if(temp>=37){
            rst = sym.equals("Y")?"A":"B";
            if(rst.equals("A")){
                a += 1;
            }else{
                b += 1;
            }
        }else{
            rst = sym.equals("Y")?"C":"D";
            if(rst.equals("C")){
                c += 1;
            }else{
                d += 1;
            }
        }
    }
    String finRst = (a>=2)?"E":"N";
    System.out.print(finRst);
    sc.close();
    }
}