import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = 0;
        for (int i = 0; i < 6; i++) {
            double number = sc.nextDouble();
            if (number > 0)
                count++;
        }
        System.out.printf("%d valores positivos\n",count);
    }
}