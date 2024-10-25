import java.util.*;
public class Ejercicio_25 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Indicar si un elemento existe en un array usando una función.
		*/
        Scanner scanner = new Scanner(System.in);

        System.out.print("¿Cuántos elementos tendrá el vector? ");
        int n = scanner.nextInt();
        int[] array = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Dime el elemento " + (i + 1) + " del vector: ");
            array[i] = scanner.nextInt();
        }

        System.out.print("¿Que numero quieres buscar? ");
        int elemento = scanner.nextInt();

        boolean existe = elementoExiste(array, elemento);

        if (existe) {
            System.out.println("El elemento " + elemento + " existe en el array.");
        } else {
            System.out.println("El elemento " + elemento + " NO existe en el array.");
        }

    }

    public static boolean elementoExiste(int[] array, int elemento) {
        for (int num : array) {
            if (num == elemento) {
                return true;
            }
        }
        return false; 
		
	}

}
