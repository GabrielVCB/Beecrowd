import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = 0;
        double soma = 0;
        for (int i = 0; i < 6; i++) {
            double number = sc.nextDouble();
            if (number > 0) {
                count++;
                soma+=number;
            }
        }
        double average = soma / count;
        System.out.printf("%d valores positivos\n%.1f\n",count,average);
    }
}

