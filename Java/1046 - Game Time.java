import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int tempo;
        if (a>b) {
            tempo = (24-a) + b;
        }
        else if (a==b)
            tempo = 24;
        else    
            tempo = b - a;
	    System.out.printf("O JOGO DUROU %d HORA(S)\n",tempo);
	}
}
