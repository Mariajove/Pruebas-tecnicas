import java.util.*;

public class Ejercicio5 {

    public static void main(String[] args) {
        // Pide 3 números por teclado e indica cuál es el mayor.
        Scanner escaner = new Scanner(System.in);
        int[] numeros = new int[3];

        System.out.println("Introduce el primer número:");
        numeros[0] = escaner.nextInt();

        System.out.println("Introduce el segundo número:");
        numeros[1] = escaner.nextInt();

        System.out.println("Introduce el tercer número:");
        numeros[2] = escaner.nextInt();

        Arrays.sort(numeros);

        System.out.println("El mayor número de los tres es: " + numeros[2]);
    }
}

