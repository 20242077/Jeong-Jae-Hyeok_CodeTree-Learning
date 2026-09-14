import java.util.Scanner;

class NextLevel{
    String id;
    int level;

    public NextLevel(){
        this.id = "codetree";
        this.level = 10;
    }

    public NextLevel(String id, int level){
        this.id = id;
        this.level = level;
    }
    public void show(){
        System.out.printf("user %s lv %d\n",this.id, this.level);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String id = sc.next();
        int level = sc.nextInt();
        // Please write your code here.
        NextLevel nextLevel = new NextLevel();
        nextLevel.show();
        NextLevel nextLevel2 = new NextLevel(id,level);
        nextLevel2.show();
    }
}