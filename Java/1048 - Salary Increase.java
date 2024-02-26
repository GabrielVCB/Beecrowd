import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double salario = sc.nextDouble();
        double reajuste = 0;
        int percentual = 0;

        if (salario > 0 && salario <= 400) {
            percentual = 15;
            reajuste = salario * 0.15;
        } else if (salario > 400 && salario <= 800) {
            percentual = 12;
            reajuste = salario * 0.12;
        } else if (salario > 800 && salario <= 1200) {
            percentual = 10;
            reajuste = salario * 0.10;
        } else if (salario > 1200 && salario <= 2000) {
            percentual = 7;
            reajuste = salario * 0.07;
        } else if (salario > 2000) {
            percentual = 4;
            reajuste = salario * 0.04;
        }

        double novoSalario = salario + reajuste;

        System.out.printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%\n", novoSalario, reajuste, percentual);
    }
}