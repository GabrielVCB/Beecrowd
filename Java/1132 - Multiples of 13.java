import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int x = sc.nextInt(), y = sc.nextInt(),naoDivisiveis = 0;
	    if(x>y) {
	        int a = x;
	        x = y;
	        y = a;
	    }
	    for (int count = x; count <= y; count++) {
	        if (count%13!=0)
	            naoDivisiveis+=count;
	    }
	    System.out.printf("%d%n",naoDivisiveis);
	}
}