import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int golInter = 0,golGre = 0,vInt = 0, vGre = 0, empate = 0, resposta = 1,grenal = 0;
		while (resposta == 1) {
		    golInter = sc.nextInt();
		    golGre = sc.nextInt();
		    if (golInter == golGre)
		        empate++;
		    else if (golInter > golGre)
		        vInt++;
		    else    
		        vGre++;
		    grenal++;
		    System.out.println("Novo grenal (1-sim 2-nao)");
		    resposta = sc.nextInt();
		}
		String maiorVencedor;
		if (vInt > vGre)
		    maiorVencedor = "Inter";
		else
		    maiorVencedor = "Gremio";
		System.out.printf("%d grenais\nInter:%d\nGremio:%d\nEmpates:%d\n%s venceu mais\n",grenal,vInt,vGre,empate,maiorVencedor);
	}
}
