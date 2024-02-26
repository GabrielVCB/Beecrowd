import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int distance = sc.nextInt();
        double litros = sc.nextDouble();
        double consumo = distance / litros;
        System.out.printf("%.3f km/l\n",consumo);
        sc.close();
    }
}
