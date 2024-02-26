import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int maior = 0,posicaoMaior = 0;
		for (int i = 0; i < 100; i++) {
		    int x = sc.nextInt();
		    if (x > maior) {
		        maior = x;
		        posicaoMaior = i;
		    }
		}
		System.out.printf("%d\n%d\n",maior,posicaoMaior + 1);
		sc.close();
	}
}
