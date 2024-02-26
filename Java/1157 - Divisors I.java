import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		for (int number = 1; number <= x; number++) {
		    if (x%number==0) {
		        System.out.printf("%d%n",number);
		    }
		}
		sc.close();
	}
}
