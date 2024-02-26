import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int testCases = sc.nextInt(),x = 0,y = 0;
	    for (int i = 0; i < testCases; i++) {
	        x = sc.nextInt();
	        y = sc.nextInt();
	        if (y==0)
	            System.out.println("divisao impossivel");
	        else {
	            double divisao =  (double)x / y;
	            System.out.printf("%.1f%n",divisao);
	        }
	    }
	}
}