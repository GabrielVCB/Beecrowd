import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt(),sum = 0;
        while (number != 0) {
            if (number%2==0) {
                for (int i = 0; i < 5; i++) {
                    sum+=number;
                    number+=2;
                }
                System.out.printf("%d\n", sum);
                sum = 0;
            }
            else {
                number++;
                for (int i = 0; i < 5; i++) {
                    sum+=number;
                    number+=2;
                }
                System.out.printf("%d\n", sum);
                sum = 0;
            }
        number = sc.nextInt();
        }
    }
}
