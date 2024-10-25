import java.util.*;
public class Ejercicio_20 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Crea un array de numeros y obten la suma y la media de sus elementos.
		*/
        Scanner scanner = new Scanner(System.in);
        System.out.print("¿Cuántos números quieres ingresar? ");
        int n = scanner.nextInt();
        int[] numbers = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Ingresa el número " + (i + 1) + ": ");
            numbers[i] = scanner.nextInt();
        }
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        double average = (double) sum / numbers.length;

        System.out.println("La suma de los elementos es: " + sum);
        System.out.println("La media de los elementos es: " + average);
	}

}
