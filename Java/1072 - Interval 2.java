import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt(), number = 0,in = 0, out = 0;
        for (int count = 0; count < cases; count++) {
            number = sc.nextInt();
            if (number >= 10 && number <= 20)
                in++;
            else 
                out++;
        } 
        System.out.printf("%d in\n%d out\n",in,out);
    }
}
