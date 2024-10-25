import java.util.*;

public class Ejercicio_22 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Dado dos arrays, uno con nombres de personas y otro con sus edades,
	    indique cual es la persona con mas edad.
		*/
        Scanner scanner = new Scanner(System.in);
        System.out.print("¿Cuántas personas quieres ingresar? ");
        int n = scanner.nextInt();
        int[] edades = new int[n];
        String[] nombres= new String[n];
        int mayor=-100;

        for (int i = 0; i < n; i++) {
            System.out.print("Ingresa el nombre de la persona " + (i + 1) + ": ");
            nombres[i] = scanner.next();
            System.out.print("Ingresa la edad de la persona " + (i + 1) + ": ");
            edades[i] = scanner.nextInt();
            if (edades[i]>mayor) {
            	mayor=edades[i];
            }
        }
        for (int j= 0; j<n;j++)
        	if (edades[j]==mayor) {
                System.out.println("La persona mas mayor es " + nombres[j] + " con " + edades[j] + " años.");       		
        	}
	}

}
