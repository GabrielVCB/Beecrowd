import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int testCases = sc.nextInt(),total = 0,coelhos = 0,ratos = 0,sapos = 0;
	    for (int i = 0; i < testCases; i++) {
	        int quant  = sc.nextInt();
	        total+=quant;
	        char animal = sc.next().charAt(0);
	        if (animal == 'C')
	            coelhos+=quant;
	        else if (animal == 'R')
	            ratos+=quant;
	        else if (animal == 'S')
	            sapos+=quant;
	    }
	    double pCoelhos = (double)(coelhos * 100) / total;
	    double pRatos = (double)(ratos * 100) / total;
	    double pSapos = (double)(sapos * 100) / total;
	    System.out.printf("Total: %d cobaias%nTotal de coelhos: %d%nTotal de ratos: %d%nTotal de sapos: %d%nPercentual de coelhos: %.2f %%%nPercentual de ratos: %.2f %%%nPercentual de sapos: %.2f %%%n",total,coelhos,ratos,sapos,pCoelhos,pRatos,pSapos);
	}
}