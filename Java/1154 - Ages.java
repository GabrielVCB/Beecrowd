import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int age = sc.nextInt(),sum = 0,count = 0;
        while (age > 0) {
            count++;
            sum+=age;
            age = sc.nextInt();
        }
        double average = (double) sum / count;
        System.out.printf("%.2f\n",average);
    }
}
