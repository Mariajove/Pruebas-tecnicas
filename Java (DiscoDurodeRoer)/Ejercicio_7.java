import java.util.*;

public class Ejercicio_7 {

    public static void main(String[] args) {
    	/* 
    	 * Mostrar la suma de los números hasta que el usuario introduzca un -1
    	 */
        Scanner escaner = new Scanner(System.in);
        int numero;
        int valor = 0;

        System.out.println("Introduce el número que quieres que sume (introduce -1 para terminar):");
        numero = escaner.nextInt();

        while (numero != -1) {
            valor += numero; 
            System.out.println("Introduce el número que quieres que sume (introduce -1 para terminar):");
            numero = escaner.nextInt();
        }

        System.out.println("El total de la suma de los números añadidos (sin contar -1) es de " + valor);
    }
}
