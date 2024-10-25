import java.util.Scanner;

public class Ejercicio_21 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Crea un array de numeros y obten el mayor y el menor del array.
		*/
        Scanner scanner = new Scanner(System.in);
        System.out.print("¿Cuántos números quieres ingresar? ");
        int n = scanner.nextInt();
        int[] numbers = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Ingresa el número " + (i + 1) + ": ");
            numbers[i] = scanner.nextInt();
        }
        int menor=1000;
        int mayor=-1000;
        for (int j =0;j<n;j++) {
        	int compara=numbers[j];
            if (compara<menor) {
            	menor=compara;
            }
            if (compara>mayor) {
            	mayor=compara;
            }
        }

        System.out.println("El valor mas pequeño es: " + menor);
        System.out.println("El valor mas grande es: " + mayor);
	}
	
}
