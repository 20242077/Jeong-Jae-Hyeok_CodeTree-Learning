import java.util.Scanner;

class SKU {
    String id;
    int code;

    public SKU(){
        id = "codetree";
        code = 50;
    }

    public SKU(String id, int code){
        this.id = id;
        this.code = code;
    }

    public void show(){
        System.out.printf("product %d is %s\n",this.code, this.id);
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String id2 = sc.next();
        int code2 = sc.nextInt();
        // Please write your code here.
        SKU sku1 = new SKU();
        sku1.show();
        SKU sku2 = new SKU(id2,code2);
        sku2.show();
    }
}