import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int minutos = sc.nextInt();
        int distance = 2 * minutos;
        System.out.printf("%d minutos%n", distance);
        
        sc.close();
    }
}