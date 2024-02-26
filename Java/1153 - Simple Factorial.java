import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt(), fatorial = 1;
		if (x == 0  || x == 1) {
		    System.out.println("1");
		}
		else {
		    while (x > 0) {
		        fatorial*=x;
		        x--;
		    }
		}
		System.out.printf("%d%n",fatorial);
		sc.close();
	}
}
