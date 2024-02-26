import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();

        if (a >= (b + c) || b >= (a + c) || c >= (a + b)) {
            System.out.println("NAO FORMA TRIANGULO");
        } else {
            if (a * a == (b * b + c * c) || b * b == (a * a + c * c) || c * c == (a * a + b * b)) {
                System.out.println("TRIANGULO RETANGULO");
            } else if (a * a > (b * b + c * c) || b * b > (a * a + c * c) || c * c > (a * a + b * b)) {
                System.out.println("TRIANGULO OBTUSANGULO");
            } else if (a * a < (b * b + c * c) && b * b < (a * a + c * c) && c * c < (a * a + b * b)) {
                System.out.println("TRIANGULO ACUTANGULO");
            }

            if (a == b && b == c) {
                System.out.println("TRIANGULO EQUILATERO");
            } else if (a == b && b != c || a != b && b == c || a == c && c != b) {
                System.out.println("TRIANGULO ISOSCELES");
            }
        }

        scanner.close();
    }
}