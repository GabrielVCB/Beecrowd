import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		 Scanner sc = new Scanner(System.in);
		 int number = sc.nextInt();
		 int hours = sc.nextInt();
		 float workedperhour = sc.nextFloat();
		 float salary = hours * workedperhour;
		 System.out.printf("NUMBER = %d\n",number);
		 System.out.printf("SALARY = U$ %.2f\n",salary);
		 sc.close();
	}
}