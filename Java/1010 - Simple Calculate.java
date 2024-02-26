import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int code1 = sc.nextInt();
        int units1 = sc.nextInt();
        float price1 = sc.nextFloat();
        int code2 = sc.nextInt();
        int units2 = sc.nextInt();
        float price2 = sc.nextFloat();
        float total = (units1 * price1) + (units2 * price2);
        System.out.printf("VALOR A PAGAR: R$ %.2f%n", total);
        sc.close();
    }
}