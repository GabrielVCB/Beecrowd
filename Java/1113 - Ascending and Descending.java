import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = 0, y = 1;
		while (x!=y) {
		    x = sc.nextInt();
		    y = sc.nextInt();
		    if (x==y)
		        break;
		    if (x>y)
		        System.out.println("Decrescente");
		    else
		        System.out.println("Crescente");
		}
		sc.close();
	}
}
