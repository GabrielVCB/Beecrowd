import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double timeTrip = sc.nextDouble();
        int averageSpeed = sc.nextInt();
        double liters = (timeTrip / 12) * averageSpeed;
        System.out.printf("%.3f%n", liters);
        
        sc.close();
    }
}