import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int combustivel = 0, alcool = 0, gasolina = 0, diesel = 0;

        while (combustivel != 4) {
            combustivel = sc.nextInt();
            if (!(combustivel > 4 || combustivel < 1)) {
                if (combustivel == 1) {
                    alcool++;
                } else if (combustivel == 2) {
                    gasolina++;
                } else if (combustivel == 3) {
                    diesel++;
                }
            }
        }

        System.out.printf("MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d\n", alcool, gasolina, diesel);
    }
}
