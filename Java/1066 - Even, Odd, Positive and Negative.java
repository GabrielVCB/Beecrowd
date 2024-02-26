import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int pares = 0,impares = 0,positivos = 0,negativos = 0;
        for (int i = 0; i < 5; i++) {
            int number = sc.nextInt();
            if (number%2==0) 
                pares++;
            else if (number%2!=0)
                impares++;
            if (number>0)
                positivos++;
            else if (number < 0)
                negativos++;
        }
        System.out.printf("%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativo(s)\n",pares,impares,positivos,negativos);
    }
}