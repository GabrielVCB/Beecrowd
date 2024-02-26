import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double salary = sc.nextDouble();
        double taxes;
        if (salary>0 && salary<=2000) {
            System.out.println("Isento");
            return;
        }
        else if (salary>2000 && salary<=3000)
            taxes = (salary - 2000) * 0.08;
        else if (salary>3000 && salary <=4500)
            taxes = 1000 * 0.08 + (salary - 3000) * 0.18;
        else    
            taxes = 1000 * 0.08 + 1500 * 0.18 + (salary - 4500) * 0.28;
        System.out.printf("R$ %.2f\n",taxes);
        sc.close();
    }
}

