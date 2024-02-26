import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCases = sc.nextInt();
		for (int j = 0; j < testCases; j++) {
		    int x = sc.nextInt(), y = sc.nextInt(),soma = 0,current=0;
    		for (int i = 0; i < y; i++) {
    		    if (x%2==0) 
    		        x++;
    		    soma+=x;
    		    x+=2;
    		}
    		System.out.printf("%d%n",soma);
		}
		
		sc.close();
	}
}
