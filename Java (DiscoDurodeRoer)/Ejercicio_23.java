import java.util.Scanner;

public class Ejercicio_23 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Crea un array e indica si es capicua.

	    Es decir, que el array es igual tanto de izquierda a derecha como de derecha a izquierda.
		*/
		
        Scanner scanner = new Scanner(System.in);
        System.out.print("¿Cuántos numeros quieres ingresar? ");
        int n = scanner.nextInt();
        int[] numeros = new int[n];
        boolean capicua=true;

        for (int i = 0; i < n; i++) {
            System.out.print("Ingresa el numero " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();

        }
        
        for (int j= 0; j<n;j++)
        	if (numeros[j]!=numeros[n-j-1]) {
        		capicua=false;
        		break;
        	}
        if (capicua==false) {
        	System.out.print("El array NO es capicua.");
        }
        else {
        	System.out.print("El array es capicua.");
        }
	}


}
