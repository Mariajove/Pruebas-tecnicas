import java.util.*;
public class Ejercicio_24 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
    	Crea dos arrays y fusionalos en uno
		*/
	
        Scanner scanner = new Scanner(System.in);

        // Pedir la cantidad de elementos para el primer array
        System.out.print("¿Cuántos números tendrá el primer array? ");
        int n1 = scanner.nextInt();
        int[] array1 = new int[n1];

        System.out.println("Ingresa los elementos del primer array:");
        for (int i = 0; i < n1; i++) {
            System.out.print("Elemento " + (i + 1) + ": ");
            array1[i] = scanner.nextInt();
        }

        System.out.print("¿Cuántos números tendrá el segundo array? ");
        int n2 = scanner.nextInt();
        int[] array2 = new int[n2];

        System.out.println("Ingresa los elementos del segundo array:");
        for (int i = 0; i < n2; i++) {
            System.out.print("Elemento " + (i + 1) + ": ");
            array2[i] = scanner.nextInt();
        }

        int[] arrayFusionado = new int[n1 + n2];
        for (int i = 0; i < n1; i++) {
            arrayFusionado[i] = array1[i];
        }
        for (int i = 0; i < n2; i++) {
            arrayFusionado[n1 + i] = array2[i];
        }


        System.out.println("Array fusionado:");
        for (int elemento : arrayFusionado) {
            System.out.print(elemento + " ");
        }

    }
}

