import java.util.Scanner;
public class Main

{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		float x = sc.nextFloat();
		if (x<=25 && x>=0) 
		    System.out.println("Intervalo [0,25]");
		else if (x>25 && x<=50)
		    System.out.println("Intervalo (25,50]");
		else if (x>50 && x<=75)
		    System.out.println("Intervalo (50,75]");
		else if (x>75 && x<=100)
		    System.out.println("Intervalo (75,100]");
		else    
		    System.out.println("Fora de intervalo");
	}
}
