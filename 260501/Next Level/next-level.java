import java.util.Scanner;
class NextLevel{
    String id;
    int lev;

    public NextLevel(){
        this.id = "codetree";
        this.lev = 10;
    }

    public NextLevel(String id, int lev){
        this.id = id;
        this.lev = lev;
    }

    void show(){
        System.out.println("user " + id + " lv "+lev);
    }
}

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
    Scanner sc = new Scanner(System.in);

    NextLevel user1 = new NextLevel();
    user1.show();

    String id = sc.next();
    int lev = sc.nextInt();

    NextLevel user2 = new NextLevel(id,lev);
    user2.show();
    sc.close();
    }
}