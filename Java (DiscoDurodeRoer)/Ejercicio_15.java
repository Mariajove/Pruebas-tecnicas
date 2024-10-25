import java.util.Scanner;

public class Ejercicio_15 {

    public static void main(String[] args) {
        int valor = (int) (Math.random() * 100 + 1);
        Scanner entrada = new Scanner(System.in);
        int numero = 0;
        int intentos = 5;

        while (numero != valor && intentos > 0) {
            System.out.println("Dime un número:");
            numero = entrada.nextInt();

            if (numero > valor) {
                System.out.println("Más pequeño");
            } else if (numero < valor) {
                System.out.println("Más grande");
            }
            intentos--; 
        }
        
        if (numero == valor) {
            System.out.println("¡Correcto! Has adivinado el número.");
            System.out.println("Los intentos usados han sido: " + (5 - intentos));
        } else {
            System.out.println("Has consumido todos tus intentos.");
            System.out.println("El número correcto era: " + valor);
        }
    }
}
