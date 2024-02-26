import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true) {
		    int m = sc.nextInt(),n = sc.nextInt(),soma = 0;
		    if (m<=0 || n<=0)
		        break;
		    if (n>m) {
		        int a = n;
		        n = m;
		        m = a;
		    }
		    for (int i = n; i <= m; i++) {
		        System.out.printf("%d ",i);
		        soma+=i;
		    }
		    System.out.printf("Sum=%d",soma);
		    System.out.println("");
		}
	}
}

