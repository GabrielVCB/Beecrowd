import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        if (number%2!=0) {
            System.out.printf("%d\n",number);
            for (int i = 0; i < 5; i++) {
                System.out.printf("%d\n",number + 2);
                number+=2;
            }
        }
        else {
            System.out.printf("%d\n",number + 1);
            number++;
            for (int i = 0; i < 5; i++) {
                System.out.printf("%d\n",number + 2);
                number+=2;
            }
        }
    }
}