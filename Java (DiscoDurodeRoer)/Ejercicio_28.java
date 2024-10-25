import java.util.*;

public class Ejercicio_28 {

    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        System.out.print("Dime el número de filas: ");
        int m = scanner.nextInt();
        System.out.print("Dime el número de columnas: ");
        int n = scanner.nextInt();
        int[][] numbers = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("Ingresa el elemento de la fila " + (i + 1) + " y columna " + (j + 1) + ": ");
                numbers[i][j] = scanner.nextInt();
            }
        }

        System.out.print("Dime la columna que quieres sumar: ");
        int c = scanner.nextInt() - 1;

        if (c < 0 || c >= n) {
            System.out.println("Número de columna fuera de rango.");
        } else {
            int sum = 0;
            for (int i = 0; i < m; i++) {
                sum += numbers[i][c]; 
            }
            System.out.println("La suma de los elementos de la columna " + (c + 1) + " es: " + sum);
        }
    }
}


