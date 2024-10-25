import java.util.Scanner;

public class Ejercicio_27 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Pide una fila por teclado y realiza la suma de los valores de esa fila
		*/
        Scanner scanner = new Scanner(System.in);
        System.out.print("¿Dime el numero de filas: ");
        int m = scanner.nextInt();
        System.out.print("¿Dime el numero de columnas: ");
        int n = scanner.nextInt();
        int[][] numbers = new int[m][n];

        for (int i = 0; i < m; i++) {
        	for (int j = 0; j<n; j++) {
                System.out.print("Ingresa el elemento de la fila " + (i + 1) + " y columna " + (j+1) + ": ");
                numbers[i][j] = scanner.nextInt();
        	}
        }
        
        System.out.print("¿Dime la fila que quieres sumar: ");
        int f = scanner.nextInt();
        
        int sum = 0;
        for (int number : numbers[f-1]) {
            sum += number;
        }

        System.out.println("La suma de los elementos es: " + sum);
	}

}
