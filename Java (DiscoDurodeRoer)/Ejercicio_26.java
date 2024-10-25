import java.util.*;
public class Ejercicio_26 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Crea una funcion que guarde en un array numeros aleatorios 
	    entre un minimo y un maximo
		*/
		
		Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa el tamaño del array: ");
        int tamaño = scanner.nextInt();
        System.out.print("Ingresa el valor mínimo: ");
        int min = scanner.nextInt();
        System.out.print("Ingresa el valor máximo: ");
        int max = scanner.nextInt();

        int[] arrayAleatorio = generarArrayAleatorio(tamaño, min, max);

        System.out.println("Array generado con números aleatorios:");
        for (int numero : arrayAleatorio) {
            System.out.print(numero + " ");
        }

        scanner.close();
    }

    public static int[] generarArrayAleatorio(int tamaño, int min, int max) {
        int[] array = new int[tamaño];
        
        for (int i = 0; i < tamaño; i++) {
            array[i] = (int) (Math.random() * (max - min + 1)) + min;
        }
        
        return array;
    }
}

