import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int maiorAB = Math.max(a,b);
		int maior = Math.max(maiorAB,c);
		int menorAB = Math.min(a,b);
		int menor = Math.min(menorAB,c);
		int mid = (a+b+c) - (maior + menor);
		System.out.printf("%d%n%d%n%d%n%n%d%n%d%n%d%n",menor,mid,maior,a,b,c);
		
	}
}