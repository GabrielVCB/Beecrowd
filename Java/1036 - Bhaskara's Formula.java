import java.io.IOException;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    double a = sc.nextDouble(),b = sc.nextDouble(),c = sc.nextDouble();
    double delta = (b*b) - (4*a*c);
    if (delta < 0 || a == 0) {
        System.out.println("Impossivel calcular");
    }
    else {
        double r1 = (-b + Math.sqrt(delta)) / (2 * a);
        double r2 = (-b - Math.sqrt(delta)) / (2 * a);
        System.out.printf("R1 = %.5f%nR2 = %.5f%n",r1,r2);
    }
    sc.close();
    }
 
}