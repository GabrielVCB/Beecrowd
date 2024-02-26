import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int notasValidas = 0;
		double media = 0,soma = 0;
		while (notasValidas < 2) {
		    double x = sc.nextDouble();
		    if (x>10 || x<0) 
		        System.out.println("nota invalida");
            else {
            soma += x;
            notasValidas++;
            }
		}
		media = soma / 2.0;
		System.out.printf("media = %.2f\n",media);
		sc.close();
	}
}
