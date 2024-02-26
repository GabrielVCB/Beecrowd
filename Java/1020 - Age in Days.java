import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int N, quociente, resto, dias;
		
		N = sc.nextInt();

		resto = N;

		dias = 365;
		quociente = resto / dias;
		System.out.println(quociente + " ano(s)");
	    resto = resto % dias;

		dias = 30;
		quociente = resto / dias;
		System.out.println(quociente + " mes(es)");
	    resto = resto % dias;

	
		System.out.println(resto + " dia(s)");

		sc.close();
	}
}